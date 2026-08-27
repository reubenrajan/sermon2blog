Fetch the sermon transcript of the link provided. 

Use Firecrawl to retrieve the transcript or captions. If no transcript is available, do not invent one and record that the run could not publish that sermon.

Before processing, inspect the current repository skills in https://github.com/reubenrajan/sermon2blog/tree/main/transcribe-to-notion.md. This file is strictly authoritative for the workflow.

Create TWO distinct representations:
1. Raw: the complete edited cleaned transcription. It must preserve the full sermon sequence and must NOT be a summary, outline, or article. Preserve speaker wording when clear, Scripture references and quotations, stories, illustrations, meaningful first-person testimony, intentional repetition, useful jokes, prayers, declarations, exhortations, and application. Remove timestamps, unnecessary speaker labels, applause/laughter markers, stage directions, audience side conversations, non-teaching greetings/logistics, repeated conversational fillers, and obvious ASR corruption. Do not remove meaningful content merely because it is not the central teaching.
2. Study: a readable study-blog edition based on the raw transcription. It may condense spoken repetition and delivery, but must preserve the sermon meaning and teaching flow.

Do not reproduce long copyrighted worship-song lyrics. Remove those sections completely.

Perform deterministic cleanup first, then a semantic editorial review. Do not add doctrine, interpretations, theological conclusions, or claims not present in the sermon. Correct grammar without changing intentional theological terminology or distinctive phrases.

Resolve every Scripture reference in both representations with YouVersion and hyperlink every occurrence, preserving the original reference text as the link label. For KJV use the YouVersion bible/1 reference pattern. Keep translation identity intact.

Publish to the Sermons Notion database at [SERMON INDEX](https://app.notion.com/p/reubenrajan/ece7eaa53bd3465c85a4fc285bc48572?v=53a1ab590ed643e281452911904c4d67):
- Raw page name: <title>-<speaker>, Type = Raw
- Study page name: <title>-<speaker>, Type = Study

Before creating or updating either page, check duplicates using Title + Type + Date. The Raw and Study records are both expected because their Type differs. Never create the same Title + Type + Date combination twice.

Before publishing, verify: Raw is complete and not a summary; Study is separate; no accidental repeated words such as I I, the the, or that that; no accidental repeated punctuation such as .., ,, , !!, or ??; no timestamps; no stage directions; no audience conversation; no unnecessary greetings or logistics; Scripture references and important quotations remain intact; meaningful testimony remains; intentional repetition remains; useful jokes remain readable; grammar is corrected; sermon meaning is preserved; no new theological claims are added; Markdown is valid; all Scripture references are linked. Avoid publishing a sermon that is already present.
