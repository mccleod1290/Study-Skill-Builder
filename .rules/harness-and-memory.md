# Rule: the harness and memory

Set by him, 2026-10-25. Source type: log (his words). Replaces the session-hook idea, which is removed.

## The harness is the trajectory

The runtime is the DeepSeek Harness (`deepseek-ai/deepseek-harness`, MIT, opened 2026-10-25, score 4 for the facts from third-party write-ups, since the official README was not opened). It is a harness, not a model: it gives a model a shell, file edits, retrieval, planning and tool calls, and records every step as a trajectory that can be replayed. "Everything is a plugin."

What matters for us: the trajectory holds the model's reasoning **and** every tool call. The old hooks only logged tool calls and prompts, never the reasoning. So the trajectory export is the single source for how a run really went. Export it ("Download session log"), and `trajectory_distill` turns it into the self-improving loop (`skills/self_improve/`).

## Three memories

1. **Trajectory** (per run): raw, from the harness. Short-lived. The input to `trajectory_distill`.
2. **Runtime memory** (per project, across sessions): `thedotmack/claude-mem` (opened 2026-10-25, score 3, third-party write-ups only). A plugin that records tool use and session summaries into a local store (SQLite plus vector search). Optional. Use it when the harness or client supports it, to carry context between sessions. It does not replace the curated wiki.
3. **Curated memory** (long-lived, hand-shaped): `llm_wiki/` (Karpathy's LLM wiki, `skills/wiki/`). The refined, linked knowledge. This is the one that compounds. `claude-mem` is raw recall; `llm_wiki` is what we keep.

## Rules

- Do not rebuild the hooks. The trajectory already does their job and more.
- Credentials for the email step live in an env file outside the repo, never in code or chat (`skills/self_improve/trajectory_distill/references/email-setup.md`).
- Cite and grade external claims about the harness or the memory tools 1 to 5; both are graded 3 to 4 here because only secondhand write-ups were opened.
