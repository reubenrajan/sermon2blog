# Sermon2Blog

Sermon2Blog converts sermon recordings into readable study blogs.

## Source

Use a public YouTube, Spotify, or podcast link.

The transcription skill retrieves the transcript when the source provides one.

## Files

- `skills/transcribe-sermon.md` contains the transcription workflow.
- `skills/transcribe-to-notion.md` contains the Notion publishing workflow.
- `archetypes/sermons.md` contains the sermon front matter template.

## Transcription Workflow as in `transcribe-sermon.md`

1. Provide the sermon link.
2. Add the speaker name when needed.
3. Add a blog title when needed.
4. Review the transcript for accuracy.
5. Save the raw transcript in `sermons/raw/`.
6. Save the study blog in `sermons/`.
7. Add YouVersion links for Scripture references.


## Transcription Workflow as in `transcribe-to-notion.md`
1. Provide the sermon link.
2. Add the speaker name when needed.
3. Add a blog title when needed.
4. Review the transcript for accuracy.
5. Save the raw transcript in Notion with the appropriate Entity property `Type` set to `Raw`.
5. Save the study blog version of the transcript in Notion with the appropriate Entity property `Type` set to `Study`.
7. Add YouVersion links for Scripture references.