# CISSP Study Kit - File Manifest

Complete listing of all files created for the generic CISSP study kit.

## Core Documentation Files

### README.md (8.5 KB)
**Landing page for the entire project**
- What is CISSP Study Kit
- System overview with architecture diagram
- Quick start (3 steps)
- Feature list
- Supported study materials
- Troubleshooting
- License information
- Contribution guidelines

### QUICKSTART.md (4.9 KB)
**Get started in 2 minutes**
- 3-step quick start
- Basic configuration
- First study session
- Optional features overview
- File reference table
- Common questions
- Estimated timeline

### CONFIG.md (7.9 KB)
**User configuration file - Edit this to customize**
- Schedule mode (bootcamp vs self-paced)
- Domain schedule configuration
- Materials configuration (optional PDFs/PPTs)
- Transcription setup (optional)
- Audio generation settings
- Quiz length settings
- Wrong answer bank settings
- 3 complete example configurations

### STUDY-GUIDE.md (16 KB)
**Comprehensive CISSP domain guide**
- CISSP overview and exam format
- All 8 domains with:
  - Key topics
  - Memory hooks
  - Why it matters
  - Exam weight and question count
- Domain weight summary table
- Recommended study orders (3 options)
- Study tips and best practices
- Free and paid resources
- Exam day checklist
- Post-exam guidance

## Study System Prompts

### DAILY-PROMPT.md (7.9 KB)
**Run this daily in Claude Cowork for study sessions**
- Complete system prompt for Claude
- Reads CONFIG.md to adapt to user's schedule
- Sources study material (materials/transcripts/Claude knowledge)
- Runs 5-10 question daily quiz
- Provides explanations and memory hooks
- Updates WRONG-ANSWER-BANK.md automatically
- Generates optional audio study files
- Handles all edge cases (missing materials, self-paced mode, etc.)

### REVIEW-PROMPT.md (8.3 KB)
**Run this weekly for comprehensive reviews**
- Complete system prompt for weekly review quiz
- 40-question format (ISC2 standard)
- Weighted by domain importance (ISC2 exam weights)
- Weighted by user weak areas (domains with many wrongs)
- Calculates custom domain weights based on performance
- Scores against 70% passing threshold
- Compares to previous reviews
- Recommends focus areas for next week

## Tracking & Reference Files

### WRONG-ANSWER-BANK.md (8.3 KB)
**Auto-updated file tracking all wrong answers across sessions**
- Summary table showing wrong answers by domain
- Entry template with fields:
  - Question text
  - Your answer
  - Correct answer
  - Domain
  - Explanation
  - Memory hook
  - Attempts count
  - Last reviewed date
  - Source (materials/transcript/Claude)
  - Status (Active/Mastered)
- 3 complete example entries
- Usage instructions
- Domain focus suggestions
- Integration with daily and review prompts

## Advanced Features

### TRANSCRIPTION-SETUP.md (13 KB)
**Optional guide for recording and transcribing lectures**
- Why transcribe lectures
- 4 transcription tool options:
  - MacWhisper (Mac GUI) - easiest
  - Whisper CLI (cross-platform) - most flexible
  - Parakeet MLX (Mac Apple Silicon) - fastest
  - MLX Whisper (Mac alternative)
- Step-by-step setup for each tool
- Recording lectures (online, Zoom, in-person)
- Audio routing for online classes
- Transcript format and best practices
- Integration workflow example
- Troubleshooting guide
- Privacy and data handling notes
- Tool comparison table

## Meta Files

### LICENSE (1.7 KB)
**MIT License**
- Full MIT license text
- Additional notes about ISC2 trademark
- Usage rights and limitations

### .gitignore (476 B)
**Standard GitHub gitignore**
- Ignores user notes and audio files
- Ignores personal materials backups
- Ignores IDE and OS files
- Ignores Python virtual environments

### MANIFEST.md (This file)
**File listing and description**

## Directory Structure

### /materials
Directory for optional study materials
- User places PDFs, PowerPoints, etc. here
- Configured in CONFIG.md
- System extracts questions from files
- Contains .gitkeep placeholder

### /transcripts
Directory for optional lecture transcripts
- User places .txt transcript files here
- Generated via MacWhisper, Whisper, etc.
- System extracts questions from lectures
- Contains .gitkeep placeholder

### /notes
Directory for auto-generated study content
- Daily study notes (auto-created)
- Review quiz results (auto-created)
- Audio study files (if audio generation enabled)
- Contains .gitkeep placeholder

## File Statistics

| File | Size | Lines | Purpose |
|------|------|-------|---------|
| README.md | 8.5 KB | ~400 | Landing page |
| STUDY-GUIDE.md | 16 KB | ~530 | Domain reference |
| TRANSCRIPTION-SETUP.md | 13 KB | ~420 | Audio setup guide |
| CONFIG.md | 7.9 KB | ~280 | User configuration |
| DAILY-PROMPT.md | 7.9 KB | ~250 | Daily study prompt |
| REVIEW-PROMPT.md | 8.3 KB | ~320 | Weekly review prompt |
| WRONG-ANSWER-BANK.md | 8.3 KB | ~200 | Answer tracking |
| QUICKSTART.md | 4.9 KB | ~200 | Quick start guide |
| LICENSE | 1.7 KB | ~40 | MIT License |
| .gitignore | 476 B | ~30 | Git configuration |
| **TOTAL** | **~80 KB** | **~2,670** | **All documentation** |

## How Files Work Together

```
User edits CONFIG.md
       ↓
    Daily study:
    └─ Copy DAILY-PROMPT.md → Claude Cowork
       ├─ Reads CONFIG.md (schedule/settings)
       ├─ Sources material (materials/, transcripts/, or Claude)
       ├─ Runs quiz (5-10 questions)
       └─ Updates WRONG-ANSWER-BANK.md
    
    Weekly review:
    └─ Copy REVIEW-PROMPT.md → Claude Cowork
       ├─ Reads CONFIG.md (settings)
       ├─ Reads WRONG-ANSWER-BANK.md (weak areas)
       ├─ Runs quiz (40 questions, weighted)
       └─ Updates WRONG-ANSWER-BANK.md

Reference:
    - STUDY-GUIDE.md: Learn 8 domains
    - TRANSCRIPTION-SETUP.md: Record lectures (optional)
    - QUICKSTART.md: Get started fast
```

## File Dependencies

- **DAILY-PROMPT.md** depends on: CONFIG.md, materials/, transcripts/ (optional)
- **REVIEW-PROMPT.md** depends on: CONFIG.md, WRONG-ANSWER-BANK.md, materials/, transcripts/ (optional)
- **WRONG-ANSWER-BANK.md** depends on: CONFIG.md (for domain list)
- **CONFIG.md** is the hub - all prompts read it
- **STUDY-GUIDE.md** is optional reference material
- **TRANSCRIPTION-SETUP.md** is optional guide for advanced users

## Ready for GitHub

All files are:
- Properly formatted Markdown
- Free of API keys/credentials
- Free of proprietary content
- MIT Licensed for public sharing
- Ready for community contributions
- Self-contained (no external dependencies)

---

**Total package: 12 core files + 3 folder placeholders = production-ready CISSP study kit**
