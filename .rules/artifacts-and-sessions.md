# Rule: artifacts and sessions

Everything the AI produces or logs lives under one root folder: `Artifacts/`. Nothing else is a home for AI output.

```text
Artifacts/
  sessions/                                 logs, one folder per session
    <YYYY>/
      <DD-MM>/                              exactly one folder per day
        <HH-MM-SS>_<session id>/            one folder per session
          inputs.md  inputs.jsonl           every user prompt, verbatim
          prompts.md                        numbered prompt ledger
          actions.md                        every tool call by the agent
          deliverables.md                   files delivered in this run
          meta.json  events.jsonl
    LATEST.md  .index.json                  pointers, written when a session is filed
  artifacts/                                deliverables, by topic
    _groups.json                            which topics belong to which group
    <group>/                                optional. related topics, e.g. aws-saa-course
      <topic_slug>/                         one folder per topic, for its whole life
    <topic_slug>/                           an ungrouped topic
      <phase>_<what>.<ext>
      HISTORY.md                            dated change log, written by harness_clerk
```

## Rules

1. One root. All AI output goes under `Artifacts/`. Scripts, rules and skills stay where they are.
2. Sessions are dated: year, then `DD-MM`, then session. One folder per day, many sessions inside it. Never a second folder for the same day. The harness session export fills these. Do not hand-make them.
3. Artifacts are not dated. A topic can take weeks or months, so the folder and file names carry no date, no `final`, no `v2`. Dates live inside `HISTORY.md` and the session logs.
4. The artifact folder is the topic slug, lowercase with underscores: `example_topic`, `topic_two`, `web_pentest_book`. The file inside says the phase and kind: `phase1_mindmap.html`, `phase2_topic_two.html`, `phase3_exam.html`. A change overwrites the same file. The history keeps the record.
5. Related topics are grouped. Ten AWS topics for one case sit in one group folder, `Artifacts/artifacts/aws-saa-course/<topic_slug>/`. The group name is lowercase with hyphens: subject, then case or course id. The groups are listed in `Artifacts/artifacts/_groups.json`. Group on a shared case, book, or course, never on names alone. `/tidy` does the filing.
6. Exception: `Documentation/` holds guides about the harness itself (HTML, hand-kept). `/tidy` does not touch it. Everything else the AI makes goes under `Artifacts/`.
7. Every deliverable is HTML, never PDF unless he asks. See `.rules/html-deliverables.md`. Source files (`.md`, `.json`) sit beside it in the same topic folder. Grounding and the confidence grades are in `.rules/grounding-and-confidence.md`.
8. The harness trajectory records every tool call, so every file written shows in the session export. `harness_clerk` reads the export and files each new or changed file into that run's `deliverables.md` and the topic's `HISTORY.md`.
9. A session log is never edited or deleted by the AI. Compaction and sub-agent summaries do not replace it. When a summary is unclear, read the session folder.
10. Skills write to `Artifacts/artifacts/<topic_slug>/`. `harness_clerk` reads `Artifacts/sessions/` and files by topic.

## Where things live

Skills are under `skills/`, scripts under `skills/scripts/`. `REPO_MAP.md` lists them. `AGENTS.md` tells every agent to read it. Private source documents are in `user-input-learning-text/` and are git-ignored.

## The harness trajectory, not hooks

The old session hooks are gone. The harness (DeepSeek Harness, `deepseek-ai/deepseek-harness`) already records the whole run as a trajectory: every assistant reasoning step, every tool call, every result. Export it from the harness ("Download session log"), drop it under `Artifacts/sessions/<...>/trajectory.json`, and the harness has already done what the hooks tried to do, plus the reasoning the hooks never saw.

`trajectory_distill` (`skills/self_improve/trajectory_distill`) reads that export. `harness_clerk` files the run by topic.

## Limits

- The trajectory carries the model's reasoning, not only the tool calls. This is why it replaced the hooks: a hook event never carried reasoning text.
- Existing outputs under `phase_N/output/<slug>/` stay where they are. New work goes under `Artifacts/artifacts/<topic_slug>/`.
