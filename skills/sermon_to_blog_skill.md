# YouTube / Spotify Sermon-to-Blog Skill

## Purpose

Convert a YouTube video, Spotify podcast, or other sermon/podcast source into a readable study-blog Markdown document and publish it in the Sermon2Blog Hugo site.

The output must preserve the speaker's overall meaning, teaching flow, important wording, Scripture references, stories, and illustrations while removing conversational delivery artifacts.

## Required input

Ask the user for:

1. The YouTube, Spotify podcast, or sermon link.
2. Optional: speaker/preacher name if it is not clear from the source.
3. Optional: preferred blog title if different from the source title.

Do not ask the user to paste the transcript unless transcript retrieval from the supplied source is not available.

## Workflow

### 1. Resolve the source

Identify whether the link is YouTube, Spotify, a podcast page, sermon archive, or another publicly accessible media page.

Fetch the available transcript or captions.

If a transcript is not available from the source, state that clearly and ask the user to provide the transcript file.

Do not invent a transcript.

### 2. Prepare the transcript

Save the retrieved transcript as a temporary `.txt` or `.md` file.

Preserve speaker wording, Scripture references, quotations, stories, illustrations, major teaching points, and existing section headings where available.

Remove timestamps, unnecessary speaker labels, applause, laughter, music/stage directions, audience responses, greetings, event logistics, and repeated conversational fillers.

### 3. Run the Python converter

Use the accompanying `sermon_to_blog.py` tool.

Run it against the transcript.

Example:

```bash
python sermon_to_blog.py transcript.md \
  --output sermon_blog.md \
  --title "The Sacrifice of Praise" \
  --speaker "Bill Johnson" \
  --source-url "SOURCE_URL"
```

The script performs deterministic cleanup: repeated-word correction, repeated-punctuation correction, common speech-to-text correction, filler removal, paragraph cleanup, Markdown heading preservation, Scripture-reference extraction, and study-pointer generation.

### 4. Editorial pass

After running the script, perform a second editorial review.

The goal is not to rewrite the sermon into a new message.

Preserve meaning. Do not add new doctrine, introduce interpretations not present in the sermon, change theological conclusions, remove important qualifications, or alter Scripture meaning.

Improve readability by converting spoken language into written language. Do not mechanically remove repetition when repetition is clearly intentional for emphasis.

Keep jokes when they contribute to the teaching. Remove jokes that depend on audience context or delivery tone when needed, while preserving useful illustrations.

Keep meaningful first-person testimony. Remove only accidental repeated first-person phrasing.

Perform a complete grammar review without changing intentional theological terminology or distinctive phrases merely because they differ from ordinary prose.

### 5. Structure the study blog

Use a readable structure such as:

```markdown
---
title: "Title"
description: "Short description"
date: YYYY-MM-DD
speaker: "Name"
source_url: "URL"
draft: false
---

# Title

*Study Blog Edition*

**Speaker:** Name
**Source:** URL

---

## Introduction

...

## Main Teaching

...

## The Biblical Foundation

...

## Practical Application

...

## Scripture References

- Reference
- Reference

## Study Pointers

- What is the main truth being taught?
- Which Scriptures support the teaching?
- What change in thinking or practice does the teaching call for?
- Which story or illustration best explains the central point?
- How can this teaching be applied in daily life?

## Reflection

...
```

Do not force these headings if the sermon already has a strong structure. Use headings that reflect the actual content.

### 6. Publish to GitHub Pages

Every completed sermon blog must be stored in the repository under:

`content/sermons/<slug>.md`

Use the Hugo `archetypes/sermons.md` structure as the default starting point.

Set `draft: false` for posts that are ready to publish.

Commit the new post to the `main` branch. The GitHub Actions workflow at `.github/workflows/hugo.yml` builds the Hugo site and deploys it to GitHub Pages.

Do not place future sermon posts only in external storage. The GitHub repository is the canonical source for published sermon blog posts.

### 7. Final quality check

Before publishing, verify:

- No accidental repeated words such as `I I`, `the the`, or `that that`.
- No accidental repeated punctuation such as `..`, `,,`, `!!`, or `??`.
- No timestamps.
- No `[applause]`, `[laughter]`, or stage directions.
- No audience conversation.
- No unnecessary greetings or event logistics.
- Scripture references remain intact.
- Important quotations remain intact.
- First-person testimony remains when meaningful.
- Jokes are readable in written form.
- Paragraphs are readable.
- Grammar is corrected.
- The sermon meaning is preserved.
- No new theological claims have been added.
- The output is valid Markdown.
- The post has valid Hugo front matter.
- The post is stored under `content/sermons/`.

## Output

Return the completed study-blog Markdown as a file and publish the same Markdown into `content/sermons/` in the `sermon2blog` repository.

Use the filename:

`<title>_Study_Blog.md`

Also provide a short summary of the editorial changes made.

## Important constraint

The Python script is the deterministic processing layer.

The editorial review is the semantic layer.

Do not replace the editorial review with aggressive automated rewriting. The purpose is to make the sermon readable as study material while preserving the original message.
