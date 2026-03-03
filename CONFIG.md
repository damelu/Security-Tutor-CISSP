# CISSP Study Kit Configuration

Edit this file to customize the system to your study plan. The daily prompt will read this file and adapt accordingly.

## Study Schedule Mode

Choose one:

### Option A: Bootcamp Mode (Fixed Schedule)

```yaml
schedule_mode: bootcamp
study_days: [monday, tuesday, wednesday, thursday, friday, saturday]
skip_days: [sunday]
```

This assumes a Monday-Saturday bootcamp schedule. Adjust `study_days` as needed.

### Option B: Self-Paced Mode

```yaml
schedule_mode: self-paced
```

In self-paced mode, you'll tell the daily prompt which domain(s) to study each time you run it.

---

## Daily Domain Schedule (Bootcamp Mode Only)

If using bootcamp mode, configure which domains to study each day.

**8 CISSP Domains:**
1. Security and Risk Management (15% exam weight)
2. Asset Security (10% exam weight)
3. Security Architecture and Engineering (12% exam weight)
4. Communication and Network Security (14% exam weight)
5. Identity and Access Management (13% exam weight)
6. Security Assessment and Testing (12% exam weight)
7. Security Operations (16% exam weight)
8. Software Development Security (8% exam weight)

**Suggested bootcamp schedule (one domain per day, repeats weekly):**

```yaml
bootcamp_schedule:
  monday: "Security and Risk Management"
  tuesday: "Asset Security"
  wednesday: "Security Architecture and Engineering"
  thursday: "Communication and Network Security"
  friday: "Identity and Access Management"
  saturday: "Security Assessment and Testing, Security Operations, Software Development Security"
```

**Customize as needed.** Example alternatives:
- **2 domains per day**: monday: "Domain1, Domain2"
- **Every other day**: monday: "Domain1", wednesday: "Domain2", etc.
- **Weighted to exam importance**: More days on Operations (16%), fewer on Software Dev (8%)

**WARNING**: Studying 3 domains in one day (as shown in the Saturday example) is **aggressive** and can lead to cognitive overload. If possible, consider:
- Splitting Saturday into two lighter days: Friday + Saturday split 6 domains across both
- Or consolidate to 2 domains max per day with lighter coverage

**Recommendation**: If using the bootcamp schedule above, take Saturday lighter on questions (5-6 instead of 8) to account for volume.

---

## Study Materials (Optional)

If you have PDFs, PowerPoints, or other materials, configure them here.

### No Materials (Claude generates questions)

```yaml
materials_path: null
materials_files: []
```

Claude will generate CISSP-standard questions from its training knowledge.

### Using Study Materials

```yaml
# Path to your materials folder (relative to this config, or absolute)
materials_path: "./materials"

# List the files to use
materials_files:
  - "ISC2-StudyGuide.pdf"
  - "Bootcamp-Slides.pdf"
  - "PracticeExams.pdf"
```

Claude will extract questions from these files during daily study.

**Supported formats:**
- PDF (best)
- PowerPoint (export to PDF recommended)
- Text files (.txt)
- Markdown (.md)

**Where to place files:** Create a `materials/` folder in this repo and place your files there.

---

## Lecture Transcription (Optional)

If you're recording lectures and transcribing them, enable this.

```yaml
enable_transcription: false
```

Change to `true` if you want the daily prompt to:
- Analyze lecture transcripts for key concepts
- Generate practice questions from lectures
- Create supplemental study audio from transcripts

### Transcription Tool

Which tool are you using to transcribe lectures?

```yaml
transcription_tool: "none"
```

Options:
- `"none"` — no transcription (default)
- `"macwhisper"` — MacWhisper GUI (Mac only)
- `"whisper-cli"` — Whisper CLI (any OS)
- `"parakeet-mlx"` — Parakeet MLX (Mac, fast)
- `"mlx-whisper"` — MLX Whisper (Mac, fast)

**Setup:** See [TRANSCRIPTION-SETUP.md](TRANSCRIPTION-SETUP.md) for installation and export instructions.

**Transcript placement:** Place `.txt` files in the `transcripts/` folder.

---

## Audio Study Files (Optional)

The daily prompt can generate TTS audio for review. Configure here.

```yaml
generate_audio: true
audio_format: "mp3"  # or "wav"
```

Audio files will be saved in `notes/audio/` and can be listened to while commuting, exercising, etc.

---

## Quiz Settings

### Daily Quiz Length

```yaml
daily_quiz_questions: 8
```

Number of questions per daily session. Typical: 5-10.

### Difficulty Mode

```yaml
difficulty_mode: "mixed"
```

Options:
- `"associate"` — Recall and identification. "What is…" / "Which of the following…"
- `"professional"` — Application and analysis. Scenario-based. "An organization discovers… what should they do first?"
- `"expert"` — Synthesis and evaluation. Multi-layered scenarios with competing priorities. "A CISO must balance… which approach BEST addresses…"
- `"mixed"` — A blend of all three tiers (recommended). Distribution below.

### Mixed Mode Distribution

```yaml
difficulty_distribution:
  associate: 0.20
  professional: 0.60
  expert: 0.20
```

In mixed mode, 20% of questions are Associate, 60% Professional, 20% Expert. This mirrors the real CISSP exam, which skews toward scenario-based reasoning. Adjust as needed — for example, early in your studies you might want `associate: 0.50, professional: 0.40, expert: 0.10`.

### Adaptive Difficulty for Weak Domains

```yaml
weak_domain_difficulty_boost: true
```

When enabled, domains where your accuracy is below 70% automatically get harder questions (one tier up). The idea: if you're getting Associate-level questions wrong, you're not ready for harder ones, so it stays. If you're acing Associate but failing Professional, it pushes you to Expert to build deeper understanding.

### Review Quiz Settings

```yaml
review_quiz_questions: 40
weekly_review_day: friday
```

Weekly review quiz has 40 questions (ISC2 standard), weighted by:
- Domain importance (ISC2 exam weight)
- Your weakness areas (from WRONG-ANSWER-BANK)
- Difficulty tier (stronger domains get harder questions)

---

## Wrong Answer Bank Settings

```yaml
# Track wrong answers by domain?
track_by_domain: true

# Include deep-dive explanations and memory hooks?
include_memory_hooks: true

# Maximum retries before removing from active review
max_retries: 3
```

---

## Your Info (Optional)

Optional: add personal info for generated notes.

```yaml
student_name: ""
study_start_date: "2026-03-03"
target_exam_date: ""
target_exam_location: ""
```

---

## Advanced: Custom Domain Weights

By default, the system uses ISC2 official exam weights. To customize (e.g., if your bootcamp emphasizes certain domains):

```yaml
custom_domain_weights:
  enabled: false
  weights:
    "Security and Risk Management": 0.15
    "Asset Security": 0.10
    "Security Architecture and Engineering": 0.12
    "Communication and Network Security": 0.14
    "Identity and Access Management": 0.13
    "Security Assessment and Testing": 0.12
    "Security Operations": 0.16
    "Software Development Security": 0.08
```

Leave `enabled: false` to use official ISC2 weights.

---

## Example Configurations

### Example 1: Bootcamp Student (Mon-Sat, with PDFs)

```yaml
schedule_mode: bootcamp
study_days: [monday, tuesday, wednesday, thursday, friday, saturday]
skip_days: [sunday]

bootcamp_schedule:
  monday: "Security and Risk Management"
  tuesday: "Asset Security"
  wednesday: "Security Architecture and Engineering"
  thursday: "Communication and Network Security"
  friday: "Identity and Access Management"
  saturday: "Security Assessment and Testing, Security Operations, Software Development Security"

materials_path: "./materials"
materials_files:
  - "ISC2-StudyGuide.pdf"
  - "Bootcamp-Slides.pdf"

enable_transcription: true
transcription_tool: "macwhisper"

daily_quiz_questions: 8
difficulty_mode: "mixed"
generate_audio: true
```

### Example 2: Self-Paced Learner (No Materials)

```yaml
schedule_mode: self-paced

materials_path: null
materials_files: []

enable_transcription: false
transcription_tool: "none"

daily_quiz_questions: 5
difficulty_mode: "associate"    # Start easy, ramp up as you gain confidence
generate_audio: true
```

### Example 3: Hybrid (Self-Paced + Transcribed Lectures)

```yaml
schedule_mode: self-paced

materials_path: null
materials_files: []

enable_transcription: true
transcription_tool: "whisper-cli"

daily_quiz_questions: 10
difficulty_mode: "expert"       # Advanced — for students close to exam day
generate_audio: false
```

---

## How the Daily Prompt Uses This Config

The daily prompt will:

1. **Read this file** at the start (CONFIG.md is optional; sensible defaults apply if missing)
2. **Determine today's domains**:
   - If bootcamp mode: use the schedule above
   - If self-paced: ask you to pick domains
   - If CONFIG missing: use sensible defaults (5 questions, no materials, no transcription)
3. **Source study material**:
   - If materials are configured: extract questions from them
   - If transcription is enabled: extract questions from lecture transcripts
   - Otherwise: generate CISSP-standard questions from training data
4. **Quiz and track**: Run daily quiz, update WRONG-ANSWER-BANK.md
5. **Generate TTS-ready text** (if enabled): Create structured text for text-to-speech tools

### CONFIG is Optional

If you don't have a CONFIG.md file, the system will:
- Study all 8 domains equally (not weighted)
- Use Claude-generated questions (no materials)
- Ask you which domain to study each session (self-paced mode)
- Still track wrong answers in WRONG-ANSWER-BANK.md
- Still generate TTS-ready text

You don't *need* CONFIG.md to get started—just run DAILY-PROMPT.md and the system adapts!

---

## Quick Reference

| Setting | What It Does | Default |
|---------|-------------|---------|
| `schedule_mode` | Bootcamp or self-paced | bootcamp |
| `materials_path` | Folder with your PDFs/PPTs | null |
| `enable_transcription` | Use lecture transcripts? | false |
| `transcription_tool` | Which transcription tool | none |
| `daily_quiz_questions` | Questions per session | 8 |
| `difficulty_mode` | Question difficulty tier | mixed |
| `difficulty_distribution` | Mix ratio (associate/professional/expert) | 20/60/20 |
| `weak_domain_difficulty_boost` | Auto-upgrade difficulty for weak domains? | true |
| `generate_audio` | Create TTS study audio? | true |
| `weekly_review_day` | Day for 40Q review | friday |

---

## Support

- **Don't have materials?** Leave `materials_path: null`. Claude generates great questions.
- **Have materials but unsure about format?** PDFs work best. PPTs should be converted to PDF.
- **Transcription not working?** Check [TRANSCRIPTION-SETUP.md](TRANSCRIPTION-SETUP.md).
- **Want to change settings mid-way?** Go ahead! Edit this file anytime. Existing wrong answers stay in the bank.

---

**Ready?** Edit the settings above, then copy [DAILY-PROMPT.md](DAILY-PROMPT.md) into Claude Cowork!
