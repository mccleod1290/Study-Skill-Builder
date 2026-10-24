# Agents: start here

0. Rules that bind every answer: `.rules/grounding-and-confidence.md` (cite original documentation, grade every claim 1 to 5) `.rules/html-deliverables.md` (HTML only, PDF only on request), `.rules/brevity.md` (5 to 10 pages at most, lower is better), and `.rules/writing-and-web.md` (plain ASD-STE100-style writing, interactive HTML).
0b. `.rules/context-isolation.md`: each phase and each judge runs in its own subagent window. Hand off by file. The writer is never the judge.
0a. `.rules/phase-order-and-coverage.md`: phase 1 finishes before phase 2 starts, even when he asks for both at once. Phase 2 covers every node of the map. `python skills/scripts/check_coverage.py <slug>` must print OK.
1. Read `REPO_MAP.md`. It says where every skill, script and rule is. Do not search the tree to find a skill.
2. Read `.rules/artifacts-and-sessions.md` before writing any file. All AI output goes under `Artifacts/`.
3. Workflows are in `WORKFLOW_STUDY.md` and `WORKFLOW_EXPERT_CAPTURE.md`. Follow them. Do not capture anyone without the consent gate.
3b. Harness documentation is in `Documentation/study_os_guide.html`. Update it when hooks, skills, or rules change.
3a. To create or change a skill, use `skills/misc/skill_creator` and follow `.rules/skill-authoring.md`.
4. After you add, move or rename a skill or script, run `python skills/scripts/repo_map.py`. `python skills/scripts/repo_map.py --check` must print OK.
5. `user-input-learning-text/` holds his private source documents. Read only. Never move, edit, or commit them.
6. Three specialized agents live in `.agents/`: `depth_agent` (deeper), `range_agent` (wider), `altitude_agent` (higher). Read `.agents/README.md`. Each runs in its own window and writes skill candidates to `skill_factory/inbox/`.
7. The LLM wiki vault is `llm_wiki/`. Schema `skills/wiki/SCHEMA.md`. Use `wiki_ingest`, `wiki_query`, `wiki_lint`, and the vendored `skills/obsidian/` skills for the syntax.
8. The skill factory is `skills/skill_factory/skill_smith`. It builds runnable skills in `skill_factory/built/` and reads `skill_factory/feedback.md` back into the backlog.
9. Private by default. `llm_wiki/`, `skill_factory/`, `Artifacts/` and `user-input-learning-text/` never go public. The public skeleton is made only by `python skills/scripts/export_public.py <dest>`, which copies an allowlist and refuses on any private match.
