# YouTube / Spotify Sermon-to-Blog Skill

## Purpose

Convert a YouTube video, Spotify podcast, or other sermon/podcast source into a readable study-blog Markdown document.

The output must preserve the speaker's overall meaning, teaching flow, important wording, Scripture references, stories, and illustrations while removing conversational delivery artifacts.

## Required input

Ask the user for:

1. The **YouTube, Spotify podcast, or sermon link**.
2. Optional: speaker/preacher name if it is not clear from the source.
3. Optional: preferred blog title if different from the source title.

Do not ask the user to paste the transcript unless transcript retrieval from the supplied source is not available.

## Workflow

### 1. Resolve the source

Identify whether the link is:

- YouTube
- Spotify
- Podcast page
- Sermon archive
- Another publicly accessible media page

Fetch the available transcript or captions.

If a transcript is not available from the source, state that clearly and ask the user to provide the transcript file.

Do not invent a transcript.

### 2. Prepare the transcript

Save the retrieved transcript as a temporary `.txt` or `.md` file.

Preserve:

- speaker wording
- Scripture references
- quotations
- stories
- illustrations
- major teaching points
- existing section headings where available

Remove:

- timestamps
- speaker labels when they are not useful
- applause
- laughter
- music/stage directions
- audience responses
- greetings and event logistics
- repeated conversational fillers

### 3. Run the Python converter

Use the accompanying:

`sermon_to_blog.py`

Run it against the transcript.

Example:

```bash
python sermon_to_blog.py transcript.md   --output sermon_blog.md   --title "The Sacrifice of Praise"   --speaker "Bill Johnson"   --source-url "SOURCE_URL"
```

The script performs deterministic cleanup:

- repeated-word correction
- repeated-punctuation correction
- common speech-to-text correction
- filler removal
- paragraph cleanup
- Markdown heading preservation
- Scripture-reference extraction
- study-pointer generation

### 4. Editorial pass

After running the script, perform a second editorial review.

The goal is not to rewrite the sermon into a new message.

Apply these rules:

#### Preserve meaning

Do not:

- add new doctrine
- introduce interpretations not present in the sermon
- change theological conclusions
- remove important qualifications
- alter Scripture meaning

#### Improve readability

Convert spoken language into written language.

For example:

> "And I, I remember, you know, when I was there..."

can become:

> "I remember when I was there..."

Do not mechanically remove repetition when repetition is clearly intentional for emphasis.

#### Handle jokes and humor

Keep jokes when they contribute to the teaching.

Convert conversational delivery into written humor.

Remove:

- audience-dependent jokes
- jokes that only work because of tone or immediate context
- repeated punchlines

Keep the underlying illustration when it supports the teaching.

#### Handle "I"

Avoid unnecessary repeated first-person statements.

Do not remove meaningful first-person testimony.

Example:

> "I, I saw this happen, and I, I realized..."

becomes:

> "I saw this happen, and I realized..."

But:

> "I was there. I saw it myself."

should remain because the repetition adds emphasis.

#### Grammar

Perform a complete grammar review.

Check:

- sentence construction
- subject-verb agreement
- articles
- verb tense
- pronouns
- punctuation
- capitalization
- paragraph breaks
- quotation marks
- Scripture references

Do not "correct" intentional theological terminology or distinctive phrases merely because they differ from ordinary prose.

### 5. Structure the study blog

Use a readable structure such as:

```markdown
# Title

*Study Blog Edition*

**Speaker:** Name
**Source:** URL

---

## Introduction

...

## Main Teaching

...

## A Key Principle

...

## The Biblical Foundation

...

## The Illustration

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

### 6. Final quality check

Before returning the Markdown, verify:

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

## Output

Return the completed study-blog Markdown as a file.

Use the filename:

`<title>_Study_Blog.md`

Also provide a short summary of the editorial changes made.

## Important constraint

The Python script is the deterministic processing layer.

The editorial review is the semantic layer.

Do not replace the editorial review with aggressive automated rewriting. The purpose is to make the sermon readable as study material while preserving the original message.
