#!/usr/bin/env python3
"""Convert a sermon/podcast transcript into a readable study-blog Markdown file.

The script performs conservative editorial cleanup:
- removes audience/stage directions and common spoken fillers
- fixes repeated words and punctuation
- repairs common transcript speech errors
- preserves Markdown headings, Scripture references, and source wording
- adds a short study-pointers section
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FILLERS = [
    r"\buh\b", r"\bum\b", r"\byou know\b",
    r"\bkind of\b", r"\bsort of\b", r"\bI mean\b",
    r"\bwell,\s*", r"\bso,\s*",
]

AUDIENCE_LINE = re.compile(
    r"^\s*\[?\s*(applause|laughter|music|crowd|audience)\b[^\]]*\]?\s*$",
    re.I,
)

STAGE = re.compile(
    r"\[[^\]]*(?:applause|laughter|music|crowd|audience)[^\]]*\]"
    r"|\([^)]*(?:applause|laughter|music|crowd|audience)[^)]*\)",
    re.I,
)


def normalize(text: str) -> str:
    replacements = {
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-", "\u2026": "...", "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def clean_paragraph(text: str) -> str:
    text = STAGE.sub("", normalize(text))

    # Remove repeated words: "I I", "the the", etc.
    text = re.sub(r"\b([A-Za-z]+)(\s+\1\b)+", r"\1", text, flags=re.I)

    for pattern in FILLERS:
        text = re.sub(pattern, "", text, flags=re.I)

    # Common speech-to-text repairs.
    replacements = {
        "gonna": "going to", "wanna": "want to", "gotta": "have to",
        "could of": "could have", "would of": "would have",
        "should of": "should have",
    }
    for old, new in replacements.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text, flags=re.I)

    # Repeated punctuation and spacing errors.
    text = re.sub(r"([,.!?;:])\1+", r"\1", text)
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    text = re.sub(r"([.!?])([A-Za-z])", r"\1 \2", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


def paragraphize(text: str) -> list[str]:
    paragraphs = []
    current = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue

        # Preserve explicit Markdown headings.
        if line.startswith("#"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append(line)
            continue

        if AUDIENCE_LINE.match(line):
            continue

        current.append(line)

    if current:
        paragraphs.append(" ".join(current))

    return [p for p in paragraphs if p.strip()]


def infer_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line.lower().startswith("title:"):
            return line.split(":", 1)[1].strip()
    return fallback


def scripture_references(text: str) -> list[str]:
    books = (
        r"(?:1|2|3)?\s?(?:Samuel|Kings|Chronicles|Corinthians|Thessalonians|"
        r"Timothy|Peter|John|Genesis|Exodus|Leviticus|Numbers|Deuteronomy|"
        r"Joshua|Judges|Ruth|Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|"
        r"Ecclesiastes|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|"
        r"Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|"
        r"Zechariah|Malachi|Matthew|Mark|Luke|Acts|Romans|Galatians|"
        r"Ephesians|Philippians|Colossians|Titus|Philemon|Hebrews|James|Jude|"
        r"Revelation)"
    )
    pattern = rf"\b{books}\s+\d+(?::\d+(?:-\d+)?)?(?:-\d+)?\b"
    return sorted(set(re.findall(pattern, text, re.I)), key=str.lower)


def convert(transcript: str, output: str, title=None, speaker=None, source_url=None):
    source = Path(transcript)
    raw = normalize(source.read_text(encoding="utf-8", errors="replace"))
    paragraphs = paragraphize(raw)

    cleaned = []
    for p in paragraphs:
        if p.startswith("#"):
            cleaned.append(p)
        else:
            p = clean_paragraph(p)
            if len(p) > 2:
                cleaned.append(p)

    title = title or infer_title(raw, source.stem.replace("_", " ").title())
    body = "\n\n".join(cleaned)
    refs = scripture_references(body)

    out = [
        f"# {title}",
        "*Study Blog Edition*",
        "",
    ]

    if speaker:
        out += [f"**Speaker:** {speaker}", ""]
    if source_url:
        out += [f"**Source:** {source_url}", ""]

    out += [
        "---",
        "",
        "This edition has been adapted from a spoken sermon or podcast transcript "
        "into a readable study resource. Conversational delivery, audience interaction, "
        "repeated speech patterns, and stage directions have been removed. The central "
        "meaning and teaching have been preserved.",
        "",
    ]

    # Preserve transcript headings. If none exist, use one main teaching section.
    if not any(p.startswith("#") for p in cleaned):
        out += ["## The Teaching", "", body]
    else:
        out += [body]

    if refs:
        out += ["", "## Scripture References", ""]
        out += [f"- {ref}" for ref in refs]

    out += [
        "",
        "## Study Pointers",
        "",
        "- What is the main truth being taught?",
        "- Which Scripture passages support the teaching?",
        "- What change in thinking or practice does the teaching call for?",
        "- Which story or illustration best explains the central point?",
        "- How can this teaching be applied in daily life?",
        "",
        "## Reflection",
        "",
        "Read the referenced Scriptures and consider how the teaching applies "
        "to your own life.",
        "",
    ]

    Path(output).write_text("\n".join(out), encoding="utf-8")
    return Path(output)


def main():
    parser = argparse.ArgumentParser(
        description="Convert a sermon/podcast transcript into study-blog Markdown."
    )
    parser.add_argument("transcript", help="Input .txt or .md transcript")
    parser.add_argument("-o", "--output", default="sermon_blog.md")
    parser.add_argument("--title")
    parser.add_argument("--speaker")
    parser.add_argument("--source-url")
    args = parser.parse_args()

    path = convert(
        args.transcript, args.output, args.title, args.speaker, args.source_url
    )
    print(f"Created: {path}")


if __name__ == "__main__":
    main()
