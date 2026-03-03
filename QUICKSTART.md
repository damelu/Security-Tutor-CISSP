# Quick Start (2 Minutes)

Get started with the CISSP Study Kit in 3 simple steps.

---

## Step 1: Configure Your Schedule (1 minute)

Open `CONFIG.md` and choose:

**Bootcamp (fixed schedule):**
```yaml
schedule_mode: bootcamp
study_days: [monday, tuesday, wednesday, thursday, friday, saturday]
```

**Self-paced (you pick domains per session):**
```yaml
schedule_mode: self-paced
```

That's it. Leave everything else at defaults for now.

---

## Step 2: Run Your First Study Session (10-15 minutes)

1. Open `DAILY-PROMPT.md`
2. Copy the "SYSTEM PROMPT" section (everything in the triple-backticks)
3. Paste it into Claude Cowork and run it
4. Answer the quiz questions honestly
5. Review your wrong answers and memory hooks

**Result**: Your first daily study session completes. Answers go into `WRONG-ANSWER-BANK.md`.

---

## Step 3: Optional: Set Up Study Materials (optional)

Already have PDFs or PowerPoints? Add them:

1. Place files in the `materials/` folder
2. Edit `CONFIG.md`:
   ```yaml
   materials_path: "./materials"
   materials_files:
     - "StudyGuide.pdf"
     - "Bootcamp-Slides.pdf"
   ```
3. Next study session will extract questions from them

**No materials?** Leave `materials_path: null`. Claude generates CISSP questions automatically.

---

## You're Ready!

- **Daily**: Run DAILY-PROMPT.md (takes ~15 min)
- **Weekly**: Run REVIEW-PROMPT.md once per week for comprehensive reviews (takes ~45 min)
- **Track**: Check WRONG-ANSWER-BANK.md to see weak areas
- **Improve**: Use wrong answers to guide daily study focus

---

## Optional: Advanced Features

### Lecture Transcription

If recording bootcamp lectures:
1. See `TRANSCRIPTION-SETUP.md` for recording/transcription tools
2. Place transcripts in `transcripts/` folder
3. Enable in CONFIG.md: `enable_transcription: true`
4. Next daily prompt will extract lecture questions

### Audio Study Files

Enable in CONFIG.md:
```yaml
generate_audio: true
```

Daily prompts will create text-to-speech-friendly study files.

---

## What This Kit Does

```
Daily Workflow:
├─ Read your CONFIG.md (which domains today?)
├─ Quiz you (5-10 questions from materials, lectures, or Claude)
├─ Track wrong answers (auto-update WRONG-ANSWER-BANK.md)
├─ Explain concepts (with memory hooks)
└─ Generate audio (optional, for commute study)

Weekly Workflow:
├─ Take 40-question review quiz
├─ Get weighted by your weak areas
├─ Score against 70% passing threshold
└─ Update trends and recommendations
```

---

## File Reference

| File | Purpose | Read First? |
|------|---------|---|
| `README.md` | Full overview | After quickstart |
| `CONFIG.md` | YOUR configuration | **Yes, edit first** |
| `DAILY-PROMPT.md` | Daily study session | **Yes, run daily** |
| `REVIEW-PROMPT.md` | Weekly review quiz | Run weekly |
| `WRONG-ANSWER-BANK.md` | Your mistake tracker | Auto-updated |
| `STUDY-GUIDE.md` | CISSP domains & exam info | Read for context |
| `TRANSCRIPTION-SETUP.md` | How to record lectures | If recording |
| `materials/` | Your study PDFs/PPTs | Add optional files |
| `transcripts/` | Your lecture transcripts | Add if transcribing |
| `notes/` | Auto-generated study notes | Read as generated |

---

## Common Questions

**Q: Do I need study materials?**
A: No. The system works perfectly without them. Claude generates CISSP-standard questions from its training data.

**Q: What if I'm self-paced, not bootcamp?**
A: Set `schedule_mode: self-paced` in CONFIG.md. You'll tell the daily prompt which domains to study each day.

**Q: How long should I study per day?**
A: About 15 minutes for the daily quiz. Do it daily for best results.

**Q: When should I take the review quiz?**
A: Once per week (typically Friday). It's a 40-question comprehensive quiz.

**Q: Can I change my schedule later?**
A: Yes. Edit CONFIG.md anytime. Your wrong-answer bank keeps accumulating.

**Q: Is this official ISC2 material?**
A: No. It's an independent study system. Use alongside official ISC2 resources for best results.

---

## Estimated Timeline

**Bootcamp (intensive, 6-8 weeks):**
- 15 min daily study
- 1 weekly review quiz
- Estimated pass rate: 70%+

**Self-paced (leisurely, 12-16 weeks):**
- 20 min daily study, 3-4 days per week
- 1 weekly review quiz
- Estimated pass rate: 70%+

**Self-paced (aggressive, 4-6 weeks):**
- 30 min daily study, 5-6 days per week
- 2 weekly review quizzes
- Estimated pass rate: 75%+

*(Note: Your study intensity should match your target exam date. Adjust CONFIG.md as needed.)*

---

## Ready? Start Here

1. **Edit CONFIG.md** (1 minute)
2. **Copy DAILY-PROMPT.md into Claude Cowork** (10-15 minutes)
3. **Come back tomorrow and repeat**

Good luck! 🎯

---

**Next steps:**
- Read `README.md` for the full picture
- Read `STUDY-GUIDE.md` to understand the 8 domains
- Check `TRANSCRIPTION-SETUP.md` if recording lectures
- Otherwise, you're ready to start studying!
