# Transcribe Sermon and Store in Github

## Purpose

Convert a YouTube video, Spotify podcast, or other sermon/podcast source into two readable Markdown representations and publish them in the `Sermon2Blog` repo:

1. A **complete cleaned edited raw transcription** that preserves the full spoken sermon content.
2. A **Study Blog Edition** that organizes the same sermon into readable study material without changing its meaning.

The output must preserve the speaker's overall meaning, teaching flow, important wording, Scripture references, stories, illustrations, meaningful first-person testimony, intentional emphasis, and useful jokes while removing conversational delivery artifacts.

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

If a transcript is not available from the source, state that clearly and do not invent a transcript.

### 2. Prepare the transcript

Save the retrieved transcript as an `.md` file.

Preserve the full sequence of spoken content. Do not summarize the sermon when creating the Raw transcription.

Preserve:

- Speaker wording when the intended meaning is clear.
- Scripture references and Scripture quotations.
- Important quotations.
- Stories and illustrations.
- Meaningful first-person testimony.
- Intentional repetition used for emphasis.
- Useful jokes and teaching-related humor.
- Prayers, declarations, exhortations, and application spoken as part of the sermon.
- Existing section headings when available.

Remove only delivery artifacts that do not contribute meaning, including:

- Timestamps.
- Unnecessary speaker labels.
- Applause and laughter markers.
- Music or stage directions.
- Audience responses and side conversations.
- Greetings and event logistics when they are not part of the teaching.
- Repeated conversational fillers.
- Obvious speech-to-text corruption.

Do not remove meaningful content merely because it is not part of the central teaching.

### 3. Worship and copyrighted song lyrics

A sermon may contain worship songs. Remove the worship section completely.

Do not reproduce long copyrighted song lyrics from the source transcript. 

Do not replace non-song sermon content with a summary merely because the surrounding video contains music.

### 4. Perform deterministic cleanup

Perform deterministic cleanup of repeated words, repeated punctuation, common speech-to-text errors, fillers, paragraphs, Markdown headings, Scripture references, and study pointers.

Apply deterministic cleanup before semantic editorial review.

Do not use deterministic rules to remove intentional rhetorical repetition.

### 5. Editorial pass

After deterministic cleanup, perform a second editorial review.

The goal is not to rewrite the sermon into a new message.

Preserve meaning. Do not add new doctrine, introduce interpretations not present in the sermon, change theological conclusions, remove important qualifications, or alter Scripture meaning.

For the **Raw transcription**, improve readability only enough to produce a faithful cleaned transcription. Do not turn it into a summary or article.

For the **Study Blog Edition**, convert spoken language into readable study material and organize it into sections that reflect the actual sermon.

Do not mechanically remove repetition when repetition is clearly intentional for emphasis.

Keep jokes when they contribute to the teaching. Remove jokes that depend entirely on audience context or delivery tone when needed, while preserving useful illustrations.

Keep meaningful first-person testimony. Remove only accidental repeated first-person phrasing.

Perform a complete grammar review without changing intentional theological terminology or distinctive phrases merely because they differ from ordinary prose.

### 6. Create the Raw transcription

Create:

`sermons/raw/raw_<title>_<speaker>.md`

The Raw file is the **complete cleaned transcription**, not a summary.

Use the repository's `archetypes/sermons.md` structure as the default metadata starting point.

Set `draft: false` for posts that are ready to publish.

The Raw file must contain the complete sermon sequence after cleanup. It must not contain statements such as `The message explains...`, `The speaker discusses...`, or other summary language in place of the sermon itself.

### 7. Create the Study Blog Edition

Create:

`sermons/<title>_<speaker>.md`

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

## Biblical Foundation

...

## Practical Application

...

## Scripture References

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

The Study Blog Edition may condense repetition and spoken delivery while preserving the sermon meaning. It must remain faithful to the Raw transcription.

### 8. Scripture linking

If Scripture references are present in either full form, such as `Hebrews 12:2`, or short form, such as `Heb 12:2`, resolve each reference with YouVersion and hyperlink every occurrence in both the Raw transcription and Study Blog Edition.

For KJV translation, use the YouVersion `bible/1` reference pattern, for example:

`https://www.bible.com/bible/1/PRO.4.23.KJV`

Preserve the original Scripture reference text as the link label.

Do not silently change the translation named or implied by the sermon.

### 9. Publish to GitHub

Every completed sermon must have both representations in the repository:

`sermons/raw/raw_<title>_<speaker>.md`

and

`sermons/<title>_<speaker>.md`

Commit both files to the `main` branch.

Do not place future sermon posts only in external storage. The GitHub repository is the canonical source for sermon posts.

### 10. Final quality check

Before publishing, verify:

- The Raw file contains the complete cleaned transcription, not a summary.
- The Study Blog Edition is distinct from the Raw transcription.
- No accidental repeated words such as `I I`, `the the`, or `that that`.
- No accidental repeated punctuation such as `..`, `,,`, `!!`, or `??`.
- No timestamps.
- No `[applause]`, `[laughter]`, or stage directions.
- No audience conversation.
- No unnecessary greetings or event logistics.
- Scripture references remain intact.
- Important quotations remain intact.
- First-person testimony remains when meaningful.
- Intentional rhetorical repetition remains.
- Jokes are readable in written form when useful.
- Paragraphs are readable.
- Grammar is corrected.
- The sermon meaning is preserved.
- No new theological claims have been added.
- The output is valid Markdown.
- The Raw post is stored under `sermons/raw/`.
- The Study Blog post is stored under `sermons/`.
- All Scripture references are hyperlinked in both representations.
- The same sermon has not already been.

## Output

Return both completed Markdown representations and publish both into the repository.

Use the filenames:

`raw_<title>_<speaker>.md`

and

`<title>_<speaker>.md`

## Important constraints

- Deterministic cleanup is the processing layer.
- Editorial review is the semantic layer.
- Do not replace editorial review with aggressive automated rewriting.
- The Raw representation is a complete cleaned transcription, not a summary.
- The Study Blog representation is the readable study edition, not a replacement for the Raw transcription.
- Never invent missing transcript content.
- Never alter theological meaning to improve prose.
