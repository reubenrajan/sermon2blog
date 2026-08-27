# Transcribe Sermon and Blogify to Notion
## Purpose
Transcribe a sermon available on YouTube video, Spotify podcast, or other sermon/podcast source into a readable study-blog Markdown document and publish it in the Notion Sermon database.

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
Fetch the available transcript or captions using Firecrawl CHATGPT plugin.
If a transcript is not available from the source, state that clearly and ask the user to provide the transcript file.
Do not invent a transcript.

### 2. Prepare the transcript

Save the retrieved transcript as a temporary `.txt` or `.md` file.
Preserve speaker wording, Scripture references, quotations, stories, illustrations, major teaching points, and existing section headings where available.
Remove timestamps, unnecessary speaker labels, applause, laughter, music/stage directions, audience responses, greetings, event logistics, and repeated conversational fillers.

### 3. Perform deterministic cleanup

Perform deterministic cleanup of repeated words, repeated punctuation, common speech-to-text errors, fillers, paragraphs, Markdown headings, Scripture references, and study pointers.

### 4. Editorial pass

After deterministic cleanup, perform a second editorial review.

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
description: "Short summary of the transcribed message"
date: YYYY-MM-DD
speaker: "Name"
source_url: "URL"
draft: false
tags: "Multiple Tags"
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

### 6. Publish to Notion

1. Every plain transcribed sermon must be stored in the Sermons Notion database with the page name as `<title>-<speaker>` with the entity property `Type` set to `Raw` 

2. Create the study blog edition of the transcribed sermon must be stored in the Sermons Notion database with the page name as `<title>-<speaker>` with the entity property `Type` set to `Study`

Always check for duplicate entry by validating the entity properties - `Title`,  `Type` and `Date`

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
- The post is stored under `sermons/`.
- `rss.xml` is valid RSS 2.0 XML and includes every non-draft sermon entry exactly once, with the raw-sermon URL and any available study-blog URL.
- If Scripture references are present in either full form, such as `Hebrews 12:2`, or short form, such as `Heb 12:2`, resolve each reference with YouVersion and hyperlink every occurrence in the raw transcription and study-blog edition. For KJV transalation use this as reference `https://www.bible.com/bible/1/PRO.4.23.KJV` where `bible/1` is the numerical index for the KJV transalation.
- Preserve the original reference text as the link label, and use a stable YouVersion Bible URL for the resolved reference.

## Important constraint
Deterministic cleanup is the processing layer. The editorial review is the semantic layer.
Do not replace the editorial review with aggressive automated rewriting. The purpose is to make the sermon readable as study material while preserving the original message.
