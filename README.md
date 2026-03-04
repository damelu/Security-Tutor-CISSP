# CISSP Training Camp 2026 — AI Study Kit

A classmate built this system using Claude (Cowork mode) to automate nightly CISSP homework. It quizzes you from the course materials, explains every answer, tracks what you get wrong, and generates audio review files you can listen to on your commute.

You need two things: the course materials you already have, and a Claude account with Cowork mode.

---

## Setup (5 minutes)

### Step 1 — Copy the course files into this folder

Place these files (from the Student files you received on day one) into the `Student files/` folder:

```
Student files/
├── CISSP v9.1 - Practice Exam.pdf
├── CISSP v9.1 Practice Exam nightly question numbers.xlsx
├── CISSP Q v12-25.pptx
├── CryptoDiagrams.pptx
├── 1 The-CCCure-CISSP-2021-CBK-Update-Study-Guide.pdf
└── Example sources for obtaining CPE credits.docx
```

You should already have all of these from class.

### Step 2 — Open Claude Cowork

Open the Claude desktop app. Switch to Cowork mode. Select this entire folder as your workspace.

### Step 3 — Start your nightly session

Open `DAILY-PROMPT.md`, copy the prompt, replace `[DAY]` with today's day, and paste it into a new Cowork chat. That's it — Claude takes over from there.

---

## How It Works

Every night after class, you start a new Cowork chat and paste the daily prompt. Claude will:

1. **Extract your homework questions** — reads the Excel tracker to find tonight's question numbers, pulls them from the PDF
2. **Quiz you one at a time** — shows each question, waits for your answer, tells you right or wrong
3. **Explain every answer** — why the correct answer is correct, why each distractor is wrong, connected to what the professor taught
4. **Move to the v12 PPT** — quizzes you on today's domains from the PowerPoint deck
5. **Track your wrong answers** — after you're done, tell Claude which questions you got wrong
6. **Deep dive on mistakes** — for each wrong answer, Claude breaks down the question, explains the trap, and gives you a memory hook
7. **Generate audio review** — creates a TTS file covering only the concepts you got wrong, ready for tomorrow's commute

---

## Local Web UI — Homework Quiz + Wrong Answer Tracker

Open `web/index.html` in any browser — no server, no install, no API key. All 426 course questions are embedded from both your materials:

| Day | Practice Exam (PDF) | PowerPoint (PPT) | Total |
|-----|--------------------:|------------------:|------:|
| Monday (D1 & 2) | 30 | 62 | **92** |
| Tuesday (D3) | 21 | 44 | **65** |
| Wednesday (D3 & 4) | 16 | 75 | **91** |
| Thursday (D4, 5 & 6) | 11 | 66 | **77** |
| Friday (D7 & 8) | 46 | 55 | **101** |

### Features

- **Tonight's Study** — pick your day and it quizzes you on all questions for those domains. Choose Practice Exam, PowerPoint, or both.
- **Re-Quiz Wrong** — filter by domain, auto-selects your weakest areas. Tracks mastery so you stop seeing questions you've nailed.
- **Custom Quiz** — 240 additional AI-generated questions at 3 difficulty tiers (associate, professional, expert) with CAT-adaptive mode.
- **Bank Sync** — paste your `WRONG-ANSWER-BANK.md` from Cowork sessions to import wrong answers directly.
- **Source tagging** — every question shows where it came from (Practice Exam PDF Q#, PPT Slide #, or AI-generated).

### Progress saves automatically

Your quiz history, wrong answers, and mastery tracking save to your browser's localStorage after every action — you don't need to do anything. Just open the file each night and your data is there.

The **Backup to File** and **Restore from File** buttons in the top right are only for two situations: if you want to back up your data as a file, or if you need to transfer your progress to a different browser or device. You don't need to use these for daily studying.

---

## Weekly Schedule

| Day | Domains | Topics |
|-----|---------|--------|
| Monday | 1 & 2 | Security & Risk Management, Asset Security |
| Tuesday | 3 | Security Architecture & Engineering |
| Wednesday | 3 & 4 | Security Architecture & Engineering, Communication & Network Security |
| Thursday | 4, 5 & 6 | Communication & Network Security, IAM, Security Assessment & Testing |
| Friday | 7 & 8 | Security Operations, Software Dev Security |
| Saturday | — | EXAM |

---

## Homework Priority (Every Night)

1. **PDF v9.1 + Excel tracker** — the Excel sheet tells you which question numbers to do each night
2. **CISSP Q v12-25.pptx** — do all questions for today's domains (in domain order)
3. **ISC2 Official CISSP Sybex Book** (online) — supplementary practice from a different source
4. **End-of-night review** — tell Claude your wrong answers, get the deep dive and audio file

---

## Folder Structure

```
CISSP-Study-Kit/
├── README.md                ← you're reading this
├── AGENTS.md                ← Claude reads this first — file map, boundaries, trace format
├── STUDY-GUIDE.md           ← schedule, question lists, domain weights
├── DAILY-PROMPT.md          ← the prompt you paste into Claude each night
├── REVIEW-PROMPT.md         ← paste this to get re-quizzed on weak spots anytime
├── WRONG-ANSWER-BANK.md     ← auto-updated by Claude — your wrong answers all week
│
├── web/
│   └── index.html           ← open in browser — 426 course questions, auto-saves progress
│
├── Student files/           ← your course materials go here
│   ├── CISSP v9.1 - Practice Exam.pdf
│   ├── CISSP v9.1 Practice Exam nightly question numbers.xlsx
│   ├── CISSP Q v12-25.pptx
│   └── (other course files)
│
└── Student files/Nightly Notes/
    ├── Monday/              ← Claude saves all Monday outputs here
    ├── Tuesday/
    ├── Wednesday/
    ├── Thursday/
    └── Friday/
```

Each night, Claude auto-generates these files in the day's folder:

- `[day]_hw_questions.txt` — extracted practice exam questions for tonight
- `[day]_wrong_answers.md` — summary of what you got wrong and why
- `[day]_weak_spots_audio_tts.txt` — TTS-ready text file for audio review of your weak spots only (convert to audio using the tools below)

**File Validation:** Claude checks that all required course files exist before starting. If any files are missing, it will report the issue and suggest fallbacks.

---

## Study on the Go

You don't have to be at your laptop to study. Each nightly session generates review material you can take anywhere. Pick whatever fits your commute.

### At Your Laptop (Nightly Homework)

This is the core workflow — paste the daily prompt into Cowork, answer questions, review mistakes. Everything below builds on that session's output.

**With voice (hands-free):** Open Claude desktop app or ChatGPT voice mode. Upload your `WRONG-ANSWER-BANK.md` and say: *"Quiz me on my wrong answers. Read each question aloud, wait for my answer, then explain."* Go back and forth verbally — no typing. Great while cooking or winding down.

**Without voice:** Normal flow. Paste the prompt, type answers, read explanations.

### On Your Phone (Commute / Walking)

**Option 1 — NotebookLM (best for passive listening)**
Upload your nightly summary or `WRONG-ANSWER-BANK.md` to [notebooklm.google.com](https://notebooklm.google.com). Tap "Audio Overview" — it generates a 5-10 minute podcast where two AI hosts discuss your weak areas. Download the audio or listen in the NotebookLM iOS app. The conversational format helps retention more than flat TTS.

**Option 2 — Claude or ChatGPT voice on your phone**
Open the Claude iOS app (or ChatGPT). Upload `WRONG-ANSWER-BANK.md`. Say: *"Quiz me verbally on these wrong answers. One at a time. Wait for me to answer."* Fully interactive with AirPods while walking or driving.

**Option 3 — iPhone Speak Screen (zero setup)**
Sync nightly notes via iCloud, open any `.md` file in Files, swipe down from top with two fingers. iOS reads it aloud. Robotic but zero effort.

**Option 4 — macOS/Windows TTS**

*macOS:* System Settings → Accessibility → Spoken Content → "Speak Selection." Select text, press shortcut. Or Terminal: `say -f summary.md -o review.aiff`

*Windows:* Open summary in Edge → right-click → "Read aloud." Or use Narrator via Settings → Accessibility.

### Quick Reference

| Method | Platform | Effort | Quality | Interactive? |
|--------|----------|--------|---------|-------------|
| NotebookLM Audio Overview | Any (web) | Low | Best — podcast-style | No (listen only) |
| Claude/ChatGPT voice | iOS, Android | Low | Great — natural voice | Yes — verbal Q&A |
| iPhone Speak Screen | iOS | Zero | Basic — robotic | No |
| macOS Speak Selection | macOS | Zero | Basic — system voice | No |
| Windows Read Aloud (Edge) | Windows | Zero | Decent | No |
| ElevenLabs | Any (web) | Medium | Great — realistic | No |

---

## Optional: NotebookLM Integration

The [NotebookLM MCP server](https://github.com/PleasePrompto/notebooklm-mcp) lets Claude query your NotebookLM notebooks directly during study sessions. This is entirely optional — everything works without it.

### What It Does

Upload your course materials to a NotebookLM notebook once, then Claude can pull citation-backed answers during study sessions without re-reading full PDFs every time.

### Setup

**Prerequisites:** Node.js (v5+), Google account, Chrome.

**Claude Code:**
```bash
claude mcp add notebooklm npx notebooklm-mcp@latest
```

**Codex:**
```bash
codex mcp add notebooklm -- npx notebooklm-mcp@latest
```

**VS Code:**
```bash
code --add-mcp '{"name":"notebooklm","command":"npx","args":["notebooklm-mcp@latest"]}'
```

**Cursor:** Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp@latest"]
    }
  }
}
```

After installing, tell Claude: *"Log me in to NotebookLM"* — Chrome opens for Google auth. One-time setup.

### Workflow

1. Create a notebook at [notebooklm.google.com](https://notebooklm.google.com) called "CISSP Study"
2. Upload your Training Camp PDFs, slides, study guide
3. Share the notebook (get the link)
4. In Claude: *"Select my CISSP Study notebook"*
5. Claude now cross-references your materials via NotebookLM during sessions

> **Note:** The MCP server uses browser automation — the authors recommend a secondary Google account. Audio Overview generation still requires going to notebooklm.google.com manually.

---

## Optional: Obsidian Integration

If you use Obsidian, there's a vault structure with CISSP domain notes and quiz generation support. See the [generic study kit repo](https://github.com/damelu/Security-Tutor-CISSP) for the Obsidian setup guide — the domain notes work for Training Camp students too.

---

## Tips

- **Don't touch AGENTS.md** — Claude reads it automatically at the start of every session. It tells Claude where your files are, what it's allowed to do, and how to handle errors. You don't need to open it.
- Start a **new chat each night**. Don't reuse yesterday's session.
- Always select this folder as your Cowork workspace before pasting the prompt.
- When Claude asks you to answer a question, just type the letter (A, B, C, or D).
- After finishing all questions, type something like "I got questions 8, 67, and 99 wrong" and Claude runs the deep dive.
- The Excel tracker has answer keys at the bottom — don't peek until after you've attempted each question.
- The professor said to study at the **management level**, not the technical level. Claude's explanations follow this approach.
- **To review weak spots anytime**, open a new chat and paste the prompt from `REVIEW-PROMPT.md`. Claude reads your `WRONG-ANSWER-BANK.md` (which grows all week) and generates a custom quiz — mixing re-asked originals, new custom questions on the same concepts, and adjacent topics. Weighted by domain importance so Domain 1 (16%) gets more attention.
- Great times to run the review quiz: between classes, Friday night, Saturday morning before the exam.

---

## Requirements

- **Claude desktop app with Cowork mode** (paid account recommended) — download from [claude.ai](https://claude.ai), **or** any IDE with AI agent support that can read and follow the prompt files (e.g., Cursor, VS Code with Copilot, Windsurf). The kit assumes you have one of these set up and pointed at this folder.
- The course materials from Training Camp (you already have these)
- About 1–2 hours per night for homework + review

> **How it works:** You open this folder in Cowork (or your AI-enabled IDE), paste the daily prompt, and the agent takes over — quizzing you, tracking wrong answers, and generating review material. If your IDE supports AGENTS.md, the agent picks up the file map and boundaries automatically.

Good luck Saturday.
