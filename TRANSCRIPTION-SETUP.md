# Lecture Transcription Setup

Optional guide for recording and transcribing lectures so they integrate with your daily study prompts.

**Skip this if you're not recording lectures.** This is completely optional; the system works perfectly without it.

---

## Why Transcribe Lectures?

If you're in a bootcamp or taking online courses with live lectures:
- Extract key concepts and practice questions from your instructor's lessons
- Generate supplemental study questions from your exact course material
- Create audio study files from lecture highlights
- Ensure your study aligns with what your instructor emphasized

**Without transcription**: The system generates CISSP-standard questions from Claude's knowledge. That's great, but lecture-specific questions are even better.

---

## Transcription Tools

Choose one tool to record and transcribe lectures. All are free or low-cost.

### Option 1: MacWhisper (Mac Only, GUI)

**Best for**: Mac users who want a simple GUI, minimal terminal knowledge.

**What it is**: A user-friendly macOS app that records audio and transcribes using OpenAI's Whisper model.

**Steps**:

1. **Download MacWhisper**:
   - Go to https://goodsnooze.gumroad.com/l/macwhisper
   - Free or pay-what-you-want ($10-20 recommended to support developer)
   - Download the `.dmg` file

2. **Install**:
   - Open the `.dmg` file
   - Drag MacWhisper to Applications
   - Launch from Applications folder

3. **Record a Lecture**:
   - Open MacWhisper
   - Click "Record" button
   - If recording your computer's audio (online class):
     * You may need to install an audio routing tool (see "Audio Routing" below)
   - If recording from a microphone:
     * Click start and let it record
   - When done, click "Stop"

4. **Transcribe**:
   - MacWhisper will transcribe automatically
   - Review the transcript in the app
   - Choose model: "Base" (fast, 77M params) or "Small" (more accurate, 244M params)

5. **Export Transcript**:
   - Click "Export" → "Text"
   - Save as `.txt` file
   - Move to your `transcripts/` folder in this kit

6. **Add to Your Kit**:
   - Rename file: `Lecture-Domain-Name-Date.txt`
   - Example: `Lecture-Security-Risk-Management-2026-03-03.txt`
   - Enable in CONFIG.md: `enable_transcription: true`

**Pros**: Simple GUI, no terminal needed, free.
**Cons**: Mac only, requires audio routing for computer audio.

**Audio Routing for Computer Audio** (Mac):
If recording an online class or screenshare:
1. Install [Loopback](https://rogueamoeba.com/loopback/) (free trial, $29 to buy)
   - Routes your computer's audio to a virtual input
2. Or use free alternative: [SoundFlower](https://rogueamoeba.com/freebies/) (older, less reliable)
3. Set MacWhisper to record from the Loopback/SoundFlower device

---

### Option 2: Whisper CLI (Any OS, Terminal)

**Best for**: Linux/Windows users or those comfortable with command line.

**What it is**: OpenAI's Whisper speech-to-text tool run from the terminal. Free, open-source.

**Steps**:

1. **Install Python** (if not already installed):
   - Go to https://www.python.org/downloads/
   - Install Python 3.8+
   - Verify: `python3 --version` in terminal

2. **Install Whisper**:
   ```bash
   pip install openai-whisper
   ```

3. **Record a Lecture**:
   - **Option A: From microphone**:
     ```bash
     ffmpeg -f avfoundation -i :0 lecture.wav
     ```
     (Mac; substitute audio device on Linux/Windows)

   - **Option B: From file** (if you have a recording):
     ```bash
     # Use your audio file directly
     ```

   - **Option C: From Zoom/online class**:
     - Use your video conferencing tool's native recording feature
     - Or use a tool like [OBS Studio](https://obsproject.com/) (free)

4. **Transcribe**:
   ```bash
   whisper lecture.wav --model base --output_format txt --output_dir ./transcripts
   ```

   Options:
   - `--model base` (fast, less accurate) or `--model small` (more accurate)
   - `--language en` (if needed)
   - Output goes to `transcripts/` folder

5. **Review Transcript**:
   - Open `lecture.txt` in your text editor
   - Fix any obvious errors (names, proper nouns)
   - Save to `transcripts/` folder

6. **Add to Your Kit**:
   - Rename: `Lecture-Domain-Name-Date.txt`
   - Enable in CONFIG.md: `enable_transcription: true`

**Pros**: Cross-platform, free, open-source, works offline.
**Cons**: Terminal required, takes longer than MacWhisper for same quality.

**Recommended settings**:
```bash
# Fast, good for bootcamp (daily lectures)
whisper lecture.wav --model base --language en --output_format txt --output_dir ./transcripts

# More accurate, for important lectures
whisper lecture.wav --model small --language en --output_format txt --output_dir ./transcripts
```

---

### Option 3: Parakeet MLX (Mac, Fast)

**Best for**: Mac users who want speed (GPU acceleration on Apple Silicon).

**What it is**: Parakeet is Mozilla's speech-to-text engine; MLX version runs on Apple Silicon Macs (M1/M2/M3).

**Steps**:

1. **Install MLX** (Apple Silicon Mac only):
   ```bash
   pip install mlx-whisper
   ```

2. **Record a Lecture**:
   - Use built-in Mac voice recorder or OBS Studio
   - Save as `.wav` or `.mp3`

3. **Transcribe** (much faster than CPU Whisper):
   ```bash
   mlx-whisper lecture.wav
   ```

4. **Export**:
   - Transcript is saved as `lecture.txt`
   - Move to `transcripts/` folder

5. **Add to Your Kit**:
   - Rename: `Lecture-Domain-Name-Date.txt`
   - Enable in CONFIG.md: `enable_transcription: true`

**Pros**: Fastest option on Apple Silicon (5-10x faster than Whisper CLI), still free.
**Cons**: Mac only, Apple Silicon required (M1/M2/M3, not Intel).

---

### Option 4: MLX Whisper (Mac, Alternative)

**Best for**: Mac users who prefer the Whisper model with GPU acceleration.

**What it is**: Same Whisper model, but optimized for MLX on Apple Silicon.

**Steps**:

```bash
# Install
pip install mlx-whisper

# Transcribe
mlx-whisper lecture.wav --model base
```

Similar to Parakeet MLX. Same speed advantage on Apple Silicon.

---

## Recording Your Lectures

### Online/Zoom Classes

**Option A: Built-in Recording**
- Click "Record" in Zoom/Google Meet/Teams
- Video conferencing platform saves recording
- Export video/audio
- Transcribe with one of the tools above

**Option B: Screen + Audio Recording**
- Use [OBS Studio](https://obsproject.com/) (free, cross-platform)
- Set up scene with your video conferencing app
- Click "Start Recording"
- Produces `.mkv` or `.mp4` file
- Extract audio:
  ```bash
  ffmpeg -i recording.mp4 -q:a 0 -map a lecture.wav
  ```

**Option C: Computer Audio + Microphone**
- macOS: Use QuickTime → File → New Audio Recording
- Windows: Use Settings → Sound → Volume mixer → Start recording
- Alternatively, use OBS Studio (cross-platform)

### In-Person Bootcamp

Use a voice recorder app:
- **Mac**: Voice Memos app (built-in)
- **iPhone/Android**: Voice Recorder app (built-in)
- **Laptop**: Audacity (free) or OBS Studio

Hold your phone/mic near the instructor or bootcamp room speaker (if allowed).

---

## Transcript Format

After transcription, your `.txt` file should look like:

```
[Lecture: Security and Risk Management]
[Instructor: Jane Smith]
[Date: March 3, 2026]

Okay everyone, today we're talking about the CIA triad. CIA stands for Confidentiality, Integrity, and Availability. These are the three pillars of security.

Confidentiality means only authorized people can access information. Think of a locked file cabinet.

Integrity means the data hasn't been modified without authorization. Like a sealed envelope—if it's opened, you know.

Availability means the system is accessible when needed. A website that's down has low availability.

So quiz question: Which of the three is violated when a hacker modifies a database record?
Answer: Integrity. The data is no longer unchanged.

Let me give you another example...
```

**The system can parse natural-language transcripts.** No special formatting needed—just plain text from your transcription tool.

---

## Integrating with the Study Kit

### Step 1: Enable Transcription

Edit CONFIG.md:

```yaml
enable_transcription: true
transcription_tool: "macwhisper"  # or "whisper-cli", "parakeet-mlx", "mlx-whisper"
```

### Step 2: Place Transcripts in Folder

Create or use existing `transcripts/` folder:

```
cissp-study-kit-github/
├── transcripts/
│   ├── Lecture-Domain1-2026-03-03.txt
│   ├── Lecture-Domain2-2026-03-04.txt
│   └── ...
```

Naming convention: `Lecture-[Domain]-[Date].txt`

### Step 3: Run Daily Prompt

When you run DAILY-PROMPT.md:

1. The system reads your CONFIG.md (`enable_transcription: true`)
2. It looks in the `transcripts/` folder
3. It extracts key concepts and generates practice questions from lectures
4. Questions from lectures are marked "from transcripts"
5. Results go to WRONG-ANSWER-BANK.md as usual

---

## Example: Full Workflow

### Scenario: Bootcamp, Day 1

**9am-12pm**: Bootcamp class on Security and Risk Management

1. **Record the class**:
   ```bash
   # Using Zoom recording or OBS Studio
   # File saved: Bootcamp_March_3.mp4
   ```

2. **Extract audio**:
   ```bash
   ffmpeg -i Bootcamp_March_3.mp4 -q:a 0 -map a Bootcamp_March_3.wav
   ```

3. **Transcribe** (assuming Whisper CLI):
   ```bash
   whisper Bootcamp_March_3.wav --model base --output_format txt --output_dir ./transcripts
   ```
   Produces: `Bootcamp_March_3.txt`

4. **Rename and organize**:
   ```bash
   mv transcripts/Bootcamp_March_3.txt transcripts/Lecture-Security-Risk-Management-2026-03-03.txt
   ```

5. **Enable transcription** in CONFIG.md:
   ```yaml
   enable_transcription: true
   transcription_tool: "whisper-cli"
   ```

6. **Run daily prompt**:
   - Copy DAILY-PROMPT.md into Claude Cowork
   - System reads lecture transcript
   - Generates 5-8 questions including lecture content
   - You study and answer
   - Wrongs go to WRONG-ANSWER-BANK.md

**Result**: Your study is aligned with exactly what your instructor taught.

---

## Troubleshooting

### "Transcription isn't working. Claude says files aren't found."

**Solutions**:
1. Check file names in `transcripts/` folder—ensure they're `.txt` files
2. Verify `enable_transcription: true` in CONFIG.md
3. Verify `transcription_tool` is set to one of: "macwhisper", "whisper-cli", "parakeet-mlx", "mlx-whisper"
4. Ensure file paths are correct (relative to repo root)

### "Whisper/Parakeet is slow."

**Solutions**:
- Use `--model base` (faster, less accurate) instead of `--model small`
- On Apple Silicon Mac: use MLX versions (parakeet-mlx, mlx-whisper) for 5-10x speedup
- Reduce audio length (transcribe shorter clips, not full 2-hour lectures)

### "Transcript quality is poor (lots of errors)."

**Solutions**:
- Re-record with clearer audio (closer to speaker, less background noise)
- Use `--model small` or `--model medium` for better accuracy
- Manually fix obvious errors (names, proper nouns) before using

### "I don't have permissions to record (company policy)."

**Solution**: Skip transcription. The system works perfectly without it. Your daily prompts will generate CISSP-standard questions instead. You lose lecture-specific content, but gain portability and privacy.

---

## Privacy and Data

- **Local processing**: Whisper CLI and MLX versions run locally on your computer (no cloud upload)
- **MacWhisper**: Also processes locally by default
- **No cloud upload required** (unless you choose a cloud-based transcription service)
- **Your transcripts are yours**: Stored in `transcripts/` folder, never uploaded

**For privacy-sensitive environments**: Use Whisper CLI or MLX versions (fully local).

---

## Advanced: Custom Transcription

If you use a different transcription tool (e.g., Otter.ai, Rev.com, human transcriber):

1. Export the transcript as `.txt` file
2. Place in `transcripts/` folder
3. Name it: `Lecture-[Domain]-[Date].txt`
4. Enable in CONFIG.md
5. The system will use it like any other transcript

---

## Summary

| Tool | Platform | Speed | Cost | Complexity |
|------|----------|-------|------|-----------|
| MacWhisper | Mac | Fast | Free | Easiest |
| Whisper CLI | Any | Slow | Free | Medium |
| Parakeet MLX | Mac (Apple Silicon) | Fastest | Free | Medium |
| MLX Whisper | Mac (Apple Silicon) | Fastest | Free | Medium |

**Recommendation for bootcamp**: MacWhisper (easiest) or Whisper CLI (most compatible).

**Recommendation for self-paced learners**: Skip transcription, use CONFIG.md `materials_path` to point to study PDFs instead.

---

## Next Steps

1. **Record a test lecture** (5-10 minutes)
2. **Transcribe it** with your chosen tool
3. **Place it in `transcripts/`** with proper naming
4. **Enable in CONFIG.md**: `enable_transcription: true`
5. **Run DAILY-PROMPT.md** and verify the system reads your lecture

---

**Ready?** Choose a tool from above, record your next lecture, and integrate it with your study kit!
