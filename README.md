# CISSP Study Kit

A modular, AI-powered study system for CISSP exam preparation. Designed for bootcamp students, self-studiers, and online learners. Works with your own study materials—or with none at all.

## What This Is

This kit automates the CISSP exam study workflow:

- **Daily study prompts** that quiz you on configured domains
- **Wrong answer tracking** across all sessions (automatically accumulated)
- **Review quizzes** weighted by domain importance and your weakness areas
- **TTS-ready text generation** for commute/workout study (structured formats for text-to-speech)
- **Memory hook deep dives** for questions you get wrong
- **(Optional) Lecture transcription integration** if you're recording classes
- **Built-in file validation** — stops and reports if config, bank, or materials are corrupted

The system works perfectly without study materials—Claude can generate CISSP-standard questions from its training knowledge. If you have PDFs, PowerPoints, or other materials, the system can extract questions from them too.

## Requirements

- **Claude desktop app with Cowork mode** — download from [claude.ai](https://claude.ai) (free account works, paid recommended for longer sessions), **or** any IDE with AI agent support that can read and follow prompt files (e.g., Cursor, VS Code with Copilot, Windsurf, Codex). The kit assumes you have one of these set up and pointed at this folder.
- **Your study materials** (optional): PDFs, PowerPoints, websites, or nothing
- **A text editor** for CONFIG.md
- **10-15 minutes per study day** for the daily prompt

> **IDE users:** If your IDE supports AGENTS.md (Cursor, Copilot, Claude Code, Codex, etc.), the agent will automatically pick up the file map, action boundaries, and session trace format. Open this folder as your workspace, paste the daily prompt, and the agent handles the rest.

## Quick Start

> New here? See [QUICKSTART.md](QUICKSTART.md) for a step-by-step walkthrough.

### 1. Configure Your Schedule

Edit `CONFIG.md`:
- Choose **bootcamp mode** (fixed Mon-Sat schedule) or **self-paced** (pick domains per session)
- Optionally point to your study materials folder
- Optionally enable lecture transcription

### 2. Start Your First Study Day

Open the **DAILY-PROMPT.md** file, copy it into Claude Cowork, and run it. The prompt will:
- Read your CONFIG.md to adapt behavior
- Quiz you on today's configured domains
- Create/update your WRONG-ANSWER-BANK.md
- Generate optional audio files

### 3. Weekly Reviews

Once a week, use **REVIEW-PROMPT.md** to take a 40-question review quiz weighted toward your weak areas.

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│ You configure your study schedule (CONFIG.md)           │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
       ┌─────────────────────┐
       │  Daily Study Prompt │
       │  (DAILY-PROMPT.md)  │
       └────────┬────────────┘
                │
      ┌─────────┴──────────┬──────────────────┐
      │                    │                  │
      ↓                    ↓                  ↓
   ┌─────────┐      ┌─────────────┐    ┌──────────────┐
   │   Quiz  │      │  Memory     │    │  Audio Gen   │
   │         │      │  Hooks for  │    │  (Optional)  │
   │ (5-10 Q)│      │  Wrongs     │    │              │
   └────┬────┘      └─────────────┘    └──────────────┘
        │
        ↓
   ┌──────────────────────────┐
   │ Update WRONG-ANSWER-BANK │
   │ (Add/track by domain)    │
   └──────────────────────────┘
        │
        ├─────→ Weekly Review Quiz (REVIEW-PROMPT.md)
        │       (40 questions, weighted by weakness)
        │
        └─────→ Repeat for all 8 domains over time
```

## Features

- ✅ **Works offline** — no study materials required
- ✅ **Works with any materials** — PDFs, PPTs, websites, lecture transcripts
- ✅ **Modular transcription** — optional, integrates seamlessly
- ✅ **Flexible scheduling** — bootcamp, self-paced, or custom
- ✅ **Wrong answer focus** — automatically highlights weak areas
- ✅ **TTS-ready text generation** — structured text for text-to-speech on commute
- ✅ **Memory hooks** — deep dives on missed questions
- ✅ **Domain-weighted review** — quizzes adapt to ISC2 exam weights
- ✅ **Built-in validation** — checks files, validates config, reports corruption
- ✅ **Confidence tracking** — tracks whether you're guessing or confident
- ✅ **Public domain knowledge** — Claude generates questions from CISSP training data
- ✅ **Difficulty tiers** — Associate (recall), Professional (scenario), Expert (synthesis) with configurable mix
- ✅ **Local web UI** — browser-based dashboard, quiz mode, review mode, wrong answer bank viewer (no API key needed)
- ✅ **Obsidian integration** — vault structure with domain notes, quiz generator support, dataview tracking

## What Makes This Different

This is the **first open-source LLM-powered CISSP study tool**, and it brings capabilities no existing GitHub tool offers:

- **AI-generated explanations from your mistakes** — Every wrong answer gets a 2-3 sentence explanation + vivid memory hook, not just "you were wrong"
- **Domain-weighted adaptive re-quizzing** — The system re-weights questions based on YOUR weak areas, not generic difficulty
- **Wrong-answer tracking feeds study priority** — Questions you miss show up in the review quiz with higher weight; your weak domains get more attention
- **Optional lecture transcript integration** — If you're in a bootcamp or online class, the system can extract key concepts and questions from YOUR lectures
- **Confidence tracking** — Distinguish between "I know this" and "I guessed right," helping you identify conceptual gaps
- **Section-based bank organization** — Wrong answers are organized by domain for targeted review, not appended randomly

No existing open-source GitHub CISSP tool does all of this. This kit brings adaptive learning principles to CISSP prep.

### Built on Agent Experience (AX) Principles

This kit follows [AGENTS.md](https://github.com/agentsmd/agents.md) conventions and [Agent Experience](https://agent-experience.dev/) design principles:

- **AGENTS.md** at the repo root gives any AI agent instant context on the file map, action boundaries, and session trace format
- **Three-tier action boundaries** (Always / Ask first / Never) prevent hallucination and silent failures
- **Progressive disclosure** — the system prompt is lean; detailed rules live in AGENTS.md and CONFIG.md where the agent reads them on demand
- **Recoverability** — every phase validates before proceeding, with graceful fallbacks
- **Traceability** — every session ends with a structured trace log for debugging

## Supported Study Materials

You can use ANY of these with this kit:

- **PDFs**: Official ISC2 Study Guides, practice exam PDFs, textbooks
- **PowerPoints**: Bootcamp slides, instructor decks
- **Web content**: Study websites, online course notes
- **Text files**: Your own notes in plain text
- **Nothing**: Claude generates CISSP-standard questions from its training knowledge

### How to Add Materials

1. Place PDFs/PPTs in the `materials/` folder
2. Update the `materials_path` in CONFIG.md
3. List the filenames in CONFIG.md's `materials_files` section
4. On your next daily prompt, the system will extract and use them

**Note**: PDFs work best. For PowerPoints, consider exporting to PDF first.

## Optional: Lecture Transcription

If you're recording lectures (bootcamp, online course, etc.), you can enable transcription:

1. Record your lectures with MacWhisper, Whisper CLI, or Parakeet
2. Follow the setup in [TRANSCRIPTION-SETUP.md](TRANSCRIPTION-SETUP.md)
3. Place transcripts in `transcripts/` folder
4. Enable in CONFIG.md (`enable_transcription: true`)

The daily prompt will then:
- Analyze lectures for key concepts and questions
- Generate supplemental practice questions from lecture material
- Create study audio from transcript highlights

Transcription is **completely optional**—everything works without it.

## Exam Format

The CISSP exam has (as of 2026):
- **100-150 multiple-choice questions** (CAT adaptive)
- **3 hours** (including tutorial/survey time)
- **8 domains** (see STUDY-GUIDE.md for weights and recent updates)
- Passing score: ~700/1000 (70% threshold)
- **Format**: Computer Adaptive Testing (CAT) — difficulty adjusts based on your performance

This kit focuses on the domains you configure, not exam-day simulation. For timed full-exam practice, refer to official ISC2 practice exams. See **STUDY-GUIDE.md** for 2025-2026 exam updates including AI/ML security, Zero Trust, SASE, privacy expansion, and post-quantum crypto.

## Files in This Kit

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `AGENTS.md` | Agent context: file map, action boundaries, session trace format |
| `CONFIG.md` | Your study configuration (edit this!) |
| `DAILY-PROMPT.md` | Copy into Claude Cowork daily; generates daily quiz |
| `REVIEW-PROMPT.md` | Weekly review quiz (40 questions) |
| `WRONG-ANSWER-BANK.md` | Tracks all your wrong answers (auto-updated) |
| `STUDY-GUIDE.md` | CISSP domain overview & exam info |
| `TRANSCRIPTION-SETUP.md` | Optional: how to record & transcribe lectures |
| `LICENSE` | MIT License |
| `materials/` | Your study materials (PDFs, PPTs) |
| `transcripts/` | Your lecture transcripts (if using) |
| `notes/` | Auto-generated daily study notes (created by system) |
| `web/index.html` | Local web UI — open in any browser, no server needed |
| `web/questions.json` | Pre-built question bank (240 questions, 3 tiers) — also embedded in index.html |
| `OBSIDIAN-SETUP.md` | Guide: integrate with Obsidian for visual study + quiz generation |

## Local Web UI

The kit includes a browser-based study interface. No server, no install, no API key — just open a single HTML file.

### Setup

Open `web/index.html` in any browser. That's it.

All 240 questions (8 domains × 3 difficulty tiers) are embedded directly in the file. Progress is saved in your browser's local storage and can be exported/imported as JSON.

### Features

- **Dashboard** — domain accuracy bars, difficulty breakdown, streak counter, progress stats
- **Quiz Mode** — filter by domain and difficulty, set question count, choose random/weak-first/sequential mode. Interactive answer selection with instant feedback, explanations, and memory hooks
- **Wrong Answer Review** — see every question you've missed, sorted by frequency, with correct answers and explanations
- **Quiz History** — date, score, question count, and time for every quiz you've taken
- **Export/Import** — back up your progress as JSON, move between devices
- **Mobile-responsive** — works on your phone's browser too
- **Dark mode** — easy on the eyes for late-night study

---

## Study on the Go

You don't have to be at your laptop to study. The kit generates review material you can use on your commute, at the gym, or walking the dog. Here are your options — pick whatever fits.

### At Your Laptop (Nightly Homework)

This is the core workflow. Paste the daily prompt into Cowork (or your IDE), answer questions, review what you got wrong. Everything below builds on this session's output.

**With voice (hands-free studying):** Open the Claude desktop app or ChatGPT voice mode. Start a conversation, paste or upload your `WRONG-ANSWER-BANK.md`, and say: *"Quiz me on my wrong answers. Read each question aloud, wait for me to answer, then explain."* You can go back and forth verbally — no typing. Works well while cooking, stretching, or winding down.

**Without voice:** The normal flow. Paste the prompt, type your answers, read the explanations. Best for focused deep study.

### On Your Phone (Commute / Walking)

**Option 1 — NotebookLM (best for passive listening)**
Upload your nightly summary or `WRONG-ANSWER-BANK.md` to [notebooklm.google.com](https://notebooklm.google.com). Tap "Audio Overview" and it generates a 5-10 minute podcast-style conversation where two AI hosts discuss your weak areas. Download the audio or listen in the NotebookLM app (iOS). This is the highest-quality option for commute listening — the conversational format helps retention more than a flat readout.

> **Power move:** If you connect the [NotebookLM MCP server](https://github.com/PleasePrompto/notebooklm-mcp) (see Optional Integrations below), Claude can query your NotebookLM notebook directly during study sessions — no tab-switching.

**Option 2 — Claude or ChatGPT voice on your phone**
Open the Claude iOS app (or ChatGPT). Upload `WRONG-ANSWER-BANK.md` from your files. Say: *"Quiz me verbally on these wrong answers. One at a time. Wait for me to answer before explaining."* Fully interactive — the AI reads, you answer aloud, it tells you if you're right and why. Works with AirPods while walking or driving.

**Option 3 — iPhone Speak Screen (zero setup)**
Sync your nightly notes via iCloud, open any `.md` or `.txt` file in Files, swipe down from the top with two fingers. iOS reads the file aloud. Robotic but functional. No extra apps needed.

**Option 4 — macOS/Windows text-to-speech**

*macOS:* System Settings → Accessibility → Spoken Content → enable "Speak Selection." Open any summary file, select all, press the shortcut. Or from Terminal: `say -f summary.md -o review.aiff` to save as audio.

*Windows:* Open the summary in Microsoft Edge, right-click → "Read aloud." Or use Narrator: Settings → Accessibility → Narrator. PowerShell alternative: `Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak((Get-Content summary.md -Raw))`

### Quick Reference

| Method | Platform | Effort | Quality | Interactive? |
|--------|----------|--------|---------|-------------|
| NotebookLM Audio Overview | Any (web) | Low — upload file, click generate | Best — podcast-style conversation | No (listen only) |
| Claude/ChatGPT voice | iOS, Android | Low — upload file, start talking | Great — natural voice | Yes — verbal Q&A |
| iPhone Speak Screen | iOS | Zero — swipe gesture | Basic — robotic TTS | No |
| macOS Speak Selection | macOS | Zero — keyboard shortcut | Basic — system voice | No |
| Windows Read Aloud (Edge) | Windows | Zero — right-click menu | Decent — Edge voices | No |
| ElevenLabs | Any (web) | Medium — paste text, download MP3 | Great — realistic voices | No |

---

## Optional: NotebookLM Integration

The [NotebookLM MCP server](https://github.com/PleasePrompto/notebooklm-mcp) lets Claude query your NotebookLM notebooks directly during study sessions. This is optional — everything works without it.

### What It Does

Instead of tab-switching between Claude and NotebookLM, you upload your study materials to a NotebookLM notebook once, then Claude can ask it questions on your behalf. Useful if you've loaded official ISC2 guides, textbooks, or heavy PDFs into NotebookLM — Claude can pull citation-backed answers without re-reading the full documents every session.

### Setup

**Prerequisites:** Node.js (v5+), a Google account, Chrome browser.

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

After installing, tell Claude: *"Log me in to NotebookLM"* — a Chrome window opens for Google authentication. One-time setup.

### Recommended Workflow

1. Go to [notebooklm.google.com](https://notebooklm.google.com) and create a notebook called "CISSP Study"
2. Upload your study materials (PDFs, slides, the study guide)
3. Share the notebook (get the link)
4. In Claude, say: *"Select my CISSP Study notebook"* — the MCP server connects
5. During study sessions, Claude can now cross-reference your materials via NotebookLM instead of reading raw PDFs each time

> **Note:** The MCP server uses browser automation. The authors recommend using a secondary Google account rather than your primary one. Audio Overview generation is not available through the MCP — you still generate audio manually at notebooklm.google.com.

---

## Obsidian Integration

If you use Obsidian for note-taking, the kit includes a ready-made vault structure with domain study notes, quiz generator support, and progress tracking.

See [OBSIDIAN-SETUP.md](OBSIDIAN-SETUP.md) for the full setup guide. Key features:

- **8 domain overview notes** with YAML frontmatter for quiz generation
- **Wikilinks** between related domains for graph visualization
- **Progress tracking** templates (manual or Dataview-powered)
- **Symlink sync** — link your WRONG-ANSWER-BANK.md so Obsidian always shows current data
- **Quiz Generator plugin** support — generate quizzes directly from domain notes

---

## Tips for Success

1. **Daily consistency beats cramming** — 30 min/day > 5 hours once a week
2. **Focus on wrong answers** — your wrong answer bank is your study guide
3. **Use audio for review** — listen while commuting/exercising (see Study on the Go above)
4. **Rotate domains** — don't overstudy one domain; follow CONFIG.md schedule
5. **Test with your materials** — if the system can extract questions from your PDFs, it's working

## Troubleshooting

**"Claude can't read my PDFs"**
- Try exporting PowerPoints to PDF
- Large PDFs may need to be split; contact support or manually extract key sections

**"Transcription isn't working"**
- Check TRANSCRIPTION-SETUP.md for your tool setup
- Verify transcript files are in `transcripts/` folder with `.txt` extension
- Ensure `enable_transcription: true` in CONFIG.md

**"I don't have study materials—will this still work?"**
- Yes! Claude generates CISSP questions from its training knowledge
- Set `materials_path: null` in CONFIG.md
- The daily prompt will work perfectly

**"I want to change my schedule mid-way"**
- Edit CONFIG.md anytime
- The wrong answer bank is agnostic to schedule—it will continue accumulating

## Getting Help

- Check [STUDY-GUIDE.md](STUDY-GUIDE.md) for CISSP domain details
- Check [TRANSCRIPTION-SETUP.md](TRANSCRIPTION-SETUP.md) for audio recording help
- Review [WRONG-ANSWER-BANK.md](WRONG-ANSWER-BANK.md) to understand the tracking format

## License

MIT License — see [LICENSE](LICENSE) file. Free to use, modify, and share.

## Contributing

Found a bug? Want to suggest a feature? PRs welcome! This kit is designed to grow with community feedback.

---

**Ready to start?** Edit `CONFIG.md`, then copy `DAILY-PROMPT.md` into Claude Cowork. Good luck with CISSP! 🎯
