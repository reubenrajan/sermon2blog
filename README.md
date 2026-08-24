# sermon2blog

Agentic skill and tool to convert sermons in YouTube/Spotify into readable blog posts.

## Published Sermon Blog

The repository also hosts the public Sermon2Blog site:

**https://reubenrajan.github.io/sermon2blog/**

The site uses [Hugo](https://gohugo.io/) with the [Lotus Docs](https://lotusdocs.dev/docs/) theme and deploys automatically to GitHub Pages when changes are pushed to `main`.

## Publishing sermons

All future sermon blog posts belong in:

```text
content/sermons/<slug>.md
```

Use the sermon archetype as the structure for new posts:

```bash
hugo new sermons/<slug>.md
```

A sermon post should contain Hugo front matter with at least `title`, `date`, `description`, and `draft: false`, followed by the sermon content.

The normal workflow is:

1. Generate or edit the sermon Markdown.
2. Save it under `content/sermons/`.
3. Commit the change to `main`.
4. GitHub Actions builds the Hugo site and deploys it to GitHub Pages.

## Site structure

```text
content/
├── _index.md
├── about.md
└── sermons/
    └── _index.md

archetypes/
└── sermons.md

.github/
└── workflows/
    └── hugo.yml
```
