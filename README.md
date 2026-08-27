# Sermon2Blog

Sermon2Blog converts sermon recordings into readable study blogs.

## Source

Use a public YouTube, Spotify, or podcast link.

The transcription skill retrieves the transcript when the source provides one.

## Files

- `skills/transcribe-sermon.md` contains the transcription workflow.
- `sermons/raw/` contains raw sermon transcripts.
- `sermons/` contains study-blog editions.
- `archetypes/sermons.md` contains the sermon front matter template.
- `rss.xml` contains the sermon feed.

## Workflow

1. Provide the sermon link.
2. Add the speaker name when needed.
3. Add a blog title when needed.
4. Review the transcript for accuracy.
5. Save the raw transcript in `sermons/raw/`.
6. Save the study blog in `sermons/`.
7. Add YouVersion links for Scripture references.
8. Update `rss.xml`.

## RSS

Add one RSS item for each sermon.

Use the raw sermon URL for the item link and GUID.

Add the study-blog URL when that file exists.

Do not add draft sermons to the feed.

