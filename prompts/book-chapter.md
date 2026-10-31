# Prompt: book chapter — study from first principles

Copy this prompt. Fill the variables. Paste it. The twin does the rest.

---

## Variables

| var | what to put | example |
|---|---|---|
| `BOOK` | book title and edition | `Web Application Hacker's Handbook 2e` |
| `CHAPTER` | chapter number and title | `Chapter 4: Mapping the Application` |
| `SOURCE_FOLDER` | path to any source material (transcripts, notes, PDFs), relative to Digital-Twin | `Study-OS-main/Study-OS-main/user-input-learning-text/wahh/ch04` |
| `OUTPUT_FOLDER` | where to write artifacts, relative to Digital-Twin | `htb-easy-web-challs/wahh-ch04` or `Study-OS-main/Study-OS-main/Artifacts/artifacts/wahh-2e/ch04-mapping/` |
| `TOPIC` | the core topic of the chapter | `application mapping and content discovery` |
| `LABS` | related labs to anchor the map to (platform + names) | `PortSwigger: content discovery, hidden parameters; HTB: none` |
| `MY_LEVEL` | what you already know | `I've done basic recon, know Burp basics, haven't done structured mapping` |

---

## The prompt

```
I'm studying {BOOK}, {CHAPTER}.

Source material is at: {SOURCE_FOLDER}
The core topic is {TOPIC}.
Related labs: {LABS}
My current knowledge: {MY_LEVEL}

Do all of this:

1. **Phase 1 mind map.** Read the source material. Build a mind map for {TOPIC} covering every concept in the chapter, with the labs as anchors. Include prerequisite knowledge I need based on {MY_LEVEL}. Write phase1_mindmap.json and phase1_map.html (interactive, self-contained). Save under {OUTPUT_FOLDER}/.

2. **Phase 2 study page.** Build phase2_page.html that teaches {TOPIC} from first principles, following all phase 2 rules. Must include:
   - Every node from the mind map, tagged with its id
   - Inline SVG diagrams for the key concepts
   - Discovery section (if the chapter covers a vuln/technique): how to find it, when to favour, when N/A — 3 scenarios each
   - Tips & Tricks: 5-7 pin-on-monitor gimmicks
   - Knowledge Check: 3-5 self-assessment questions with collapsible answers
   - References with URLs and what each settles
   - Confidence grades (1-5) on every factual claim
   - Mark as multi-topic if it covers several concepts: <meta name="twin-budget" content="multi">
   Tailor the depth to my level: {MY_LEVEL}.

3. **Judge.** Spawn a separate agent to audit all work against CRITERIA.md and write JUDGE_REPORT.md.

4. **Update progress.** Add or update the chapter in twin/progress.md.

5. **Run twin/check.py.** Must print OK.

Save everything under {OUTPUT_FOLDER}/.
```

---

## What it triggers

- Phase 1 mapper agent (context isolation)
- Phase 2 writer agent with all 2026-11-01 rules
- Phase 2 judge agent (the writer never judges)
- Progress update (rule 3)
- Twin check (working agreement rule 4)

## What it does not trigger

- CTF exploit (no live target — add the target IP if there is one)
- Phase 3 (add `/spar` after for a Socratic spar, or ask for the examiner)
- Phase 2 visual pass (add "run the visual pass" after)
- Email (add "email it" after)

## Variations

**Multiple chapters at once:** change `CHAPTER` to a range. The page becomes multi-topic (no word limit). One mind map, one page.

**Chapter + labs together:** add the lab IPs or URLs to `LABS` and add "solve the labs first, then study" to the prompt. The twin solves them, then uses them as anchors.

**Book + CTF combo:** use the CTF prompt instead, but add `BOOK` and `CHAPTER` as context. The page covers the chapter concepts through the lens of the challenge.
