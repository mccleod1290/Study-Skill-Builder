# self_improve: the self-improving loop

The harness records every run as a trajectory: the model's reasoning and every tool call. This group turns that record into skill improvements.

| skill | does |
|---|---|
| `trajectory_distill` | reads a harness trajectory export; writes all-reasoning HTML and a gaps HTML (what the run did that the skill did not cover); emails both; files gaps to `skill_factory/feedback.md` |

## The loop

```text
run under a skill  ->  harness trajectory (reasoning + tool calls)
trajectory         ->  trajectory_distill: all reasoning, then the gaps
gaps               ->  skill_factory/feedback.md
feedback           ->  skill_smith builds the missing step; diagnostician routes it
```

This replaces the old session hooks. A hook event never carried the model's reasoning. The trajectory does, so the gap between what the skill taught and what the run actually reasoned is now visible and fixable.

Memory: see `.rules/harness-and-memory.md` for the harness (`deepseek-ai/deepseek-harness`), the runtime memory option (`thedotmack/claude-mem`), and the curated memory (`llm_wiki/`).
