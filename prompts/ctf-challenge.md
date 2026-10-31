# Prompt: CTF challenge — solve + study

Copy this prompt. Fill the variables. Paste it. The twin does the rest.

---

## Variables

| var | what to put | example |
|---|---|---|
| `TARGET` | IP:port of the live instance | `154.57.164.69:43077` |
| `PLATFORM` | HTB, TryHackMe, PicoCTF, etc. | `HTB` |
| `CHALLENGE` | challenge name | `Gunship` |
| `SOURCE_FOLDER` | path to local source code and any writeup, relative to Digital-Twin | `htb-easy-web-challs/gunship` |
| `TOPIC` | the core vulnerability or technique | `JS prototype pollution` |
| `MY_LEVEL` | what you already know about the topic (be honest) | `I know JS is a web language and I know OWASP top 10, nothing deeper` |

---

## The prompt

```
{TARGET} — this is a {PLATFORM} CTF challenge called {CHALLENGE}.

Source code and any solution/writeup are at: {SOURCE_FOLDER}

The core topic is {TOPIC}. My current knowledge: {MY_LEVEL}

Do all of this:

1. **Solve the challenge.** Read the source code first. Read the writeup if one exists. Exploit the live instance at {TARGET} and give me the flag. Use the writeup to understand the exploit chain, not to copy-paste blindly.

2. **Phase 1 mind map.** Build a mind map for {TOPIC} and all prerequisite knowledge needed to understand it from first principles. Include the challenge as an anchor. Write phase1_mindmap.json and phase1_map.html (interactive, self-contained). Save under {SOURCE_FOLDER}/.

3. **Phase 2 study page.** Build phase2_page.html that teaches {TOPIC} from scratch to exploit, following all phase 2 rules. Must include:
   - Every node from the mind map, tagged with its id
   - Inline SVG diagrams for the key concepts
   - Discovery section: how to find it, when to favour, when N/A — 3 scenarios each
   - Tips & Tricks: 5-7 pin-on-monitor gimmicks
   - Knowledge Check: 3-5 self-assessment questions with collapsible answers
   - References with URLs and what each settles
   - Confidence grades (1-5) on every factual claim
   - Mark as multi-topic: <meta name="twin-budget" content="multi">
   Tailor the depth to my level: {MY_LEVEL}. Do not assume I know things I said I do not know.

4. **Judge.** Spawn a separate agent to audit all work against CRITERIA.md and write JUDGE_REPORT.md.

5. **Update progress.** Add the lab to twin/progress.md with date, status, the why in one line, and next lab.

6. **Run twin/check.py.** Must print OK.

Save everything under {SOURCE_FOLDER}/.
```

---

## What it triggers

- CTF exploit (rule 7: authorized targets only)
- Phase 1 mapper agent (context isolation)
- Phase 2 writer agent with all 2026-11-01 rules: knowledge check, tips & tricks, discovery, richer visuals
- Phase 2 judge agent (context isolation: the writer never judges)
- Progress update (rule 3)
- Twin check (working agreement rule 4)

## What it does not trigger

- Phase 3 (no spar, no exam — add `/spar` after if you want one)
- Phase 2 visual pass (no diagrammer/web_builder/video — add "run the visual pass" after if you want it)
- Email (add "email it" after if you want it sent)
