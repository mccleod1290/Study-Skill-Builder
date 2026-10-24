# .agents: the three specialized agents

Source idea: Felix Rieseberg, "How to be more ambitious: a tutorial for humans with models", https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/ (opened 2026-10-24, score 4). The post names four directions of ambition: speed, altitude, depth, range. Speed is already a given. The other three are an agent each.

| agent | direction | reads | writes |
|---|---|---|---|
| `depth_agent` | deeper: raw data, real tools, first principles, an outside check | `llm_wiki/`, phase 1 to 4 outputs | in-depth guide, prerequisites, mental model, comparison |
| `range_agent` | wider: nouns to verbs, a crew of fields, a red team | `llm_wiki/`, phase outputs | cross-topic map, use cases, patterns, variants |
| `altitude_agent` | higher: the goal beyond the goal, urgent decisions, workflow redesign | `llm_wiki/`, roadmap, feedback | workflows, playbooks, pipelines, project plans |

## The loop

```text
Study-OS phases 1-4  --study, practice, research-->  llm_wiki/ (private)
llm_wiki/            --knowledge source-->           depth | range | altitude
the three agents     --skill candidates-->           skill_factory/inbox/ (private)
skill_smith          --runnable skills-->            skill_factory/built/ (private)
labs, CTFs, bounty   --execution feedback-->         skill_factory/feedback.md --> backlog and roadmap
```

## Rules shared by all three

1. Each agent runs in its own context window (`.rules/context-isolation.md`). Hand-off is by file.
2. No agent grades its own work. An outside judge or a check decides.
3. Do the work of a role. Do not role-play it.
4. Ground and grade every claim 1 to 5 (`.rules/grounding-and-confidence.md`).
5. The wiki and the built skills are private. They never leave this machine.

## Use with Claude Code

Claude Code loads subagents from `.claude/agents/`. Copy or link these files there:

```bash
mkdir -p .claude/agents && cp .agents/*_agent.md .claude/agents/
```
