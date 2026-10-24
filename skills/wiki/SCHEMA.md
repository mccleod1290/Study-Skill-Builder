# LLM wiki schema

Source: Andrej Karpathy, "LLM Wiki" gist, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (opened 2026-10-24, score 4). The wiki is compiled once and kept current, so a question does not start from raw documents each time. The human picks sources and asks questions. The LLM does the bookkeeping.

The vault is private. It lives at `llm_wiki/` in this repo, is git-ignored, and is never exported (`skills/scripts/export_public.py` does not copy it). Open it in Obsidian as a vault.

## Three layers

```text
llm_wiki/
  raw/                  layer 1. sources. the LLM reads them, never edits them
    assets/             images and attachments the pages embed
  wiki/                 layer 2. pages the LLM writes and links
    concepts/           one idea per page
    connections/        <a>--<b>.md, one real link between two ideas
    mental_models/      first principles, patterns, the why
    examples/           scripts, commands, tools, ready-to-use references
    sources/            one summary page per raw source
    overview.md         the whole map in one page
  index.md              catalog: every page, one line, by type
  log.md                append-only: ingest, query, lint
```

Layer 3 is this file. It tells the LLM how to keep the wiki. He and the LLM change it together.

Study-OS outputs are sources too. A finished phase 2 page under `Artifacts/artifacts/<slug>/` is ingested as a source. Do not copy it into `raw/`. Link its path.

## Page format

Obsidian Flavored Markdown (see `skills/obsidian/obsidian-markdown`). Every page starts with properties:

```yaml
---
type: concept | connection | mental_model | example | source | overview
domain: web | cloud | ai | general
tags: []
sources: [raw/... or Artifacts/artifacts/<slug>/...]
confidence: 1-5
status: exposure | practiced | solved
updated: YYYY-MM-DD
---
```

Body rules:

1. First line: one sentence that says what it is.
2. Then the parts, the condition, when it does not apply, then how.
3. Link every other page you name with `[[page-name]]`. A link to a page that does not exist yet is allowed. Lint reports it.
4. Cite each claim to a source page and keep its grade 1 to 5.
5. `status` is honest: a lab solved by copying the solution is `exposure`.

## index.md

One line per page, under a heading per type: `- [[page]] — one-line summary (sources: n, updated: date)`. Read it first on every query. Rebuild it on every ingest.

## log.md

Append only. One line per operation, same prefix every time, so `grep` works:

```text
## [YYYY-MM-DD] ingest | <source title> | pages: a, b, c
## [YYYY-MM-DD] query | <question> | filed: <page or none>
## [YYYY-MM-DD] lint | issues: n | fixed: n
```

## Operations

| operation | skill | does |
|---|---|---|
| ingest | `wiki_ingest` | one source in, 5 to 15 pages touched, index and log updated |
| query | `wiki_query` | answer from the wiki with citations, file a good answer back |
| lint | `wiki_lint` | contradictions, stale claims, orphans, missing pages, missing links, gaps |

## Scale

Up to about 100 sources and a few hundred pages, `index.md` is enough. Past that, add a local search tool. Ask before you install one.
