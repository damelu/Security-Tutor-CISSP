# Contributing to CISSP Study Kit

Thank you for your interest in contributing to this open-source CISSP study tool! We welcome bug reports, feature suggestions, and pull requests.

## How to Report Issues

Found a bug or have a question? Open a GitHub issue:

1. Go to **Issues** tab in the repository
2. Click **New Issue**
3. Choose the template (Bug Report or Feature Request)
4. Fill in details:
   - **What you were doing** when the issue occurred
   - **What you expected to happen**
   - **What actually happened**
   - **Your environment** (OS, Python version, Claude plan if applicable)
   - **Steps to reproduce** (if it's a bug)

Examples:
- "CONFIG.md loading fails with YAML error when using special characters"
- "WRONG-ANSWER-BANK.md doesn't include all entries from previous session"
- "Would like to add spaced repetition intervals to memory hook reviews"

## How to Suggest Improvements

Have an idea to make the kit better?

1. Open an issue tagged **enhancement**
2. Describe the feature:
   - **What problem does it solve?**
   - **Who would benefit?** (bootcamp students, self-studiers, etc.)
   - **How would it work?** (if you have ideas)
   - **Examples** of the feature in action

Examples:
- "Add difficulty metrics to track which question types are hardest"
- "Support for study groups — share progress anonymously"
- "Dark mode for study notes"
- "Domain-specific study timers"

## Pull Request Process

Want to contribute code or docs? We love PRs!

### Before You Start

1. **Check existing issues** — make sure someone hasn't already done this
2. **Open an issue first** (especially for large changes) — discuss the approach before coding
3. **Test prompts with Claude** before submitting — the system prompts are mission-critical

### Making Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/cissp-study-kit.git
   cd cissp-study-kit
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b improve/better-memory-hooks
   # or
   git checkout -b fix/config-validation-bug
   ```

3. **Make your changes**
   - Edit files directly (README.md, CONFIG.md, prompts, etc.)
   - Test thoroughly with Claude Cowork
   - Follow the existing style and tone

4. **Commit with clear messages**
   ```bash
   git commit -m "Add AI/ML security topics to 2025-2026 exam updates"
   git commit -m "Fix: WRONG-ANSWER-BANK section-based overwrite instead of append"
   ```

5. **Push to your fork**
   ```bash
   git push origin improve/better-memory-hooks
   ```

6. **Open a Pull Request**
   - Go to the original repository
   - Click **Pull Requests** → **New Pull Request**
   - Select your branch
   - Describe what you changed and why

### PR Guidelines

- **Test prompt changes with Claude** before submitting (run at least one full session)
- **Update documentation** if you change how the system works
- **Keep commits focused** — one feature or fix per PR
- **Write clear commit messages** — future maintainers will thank you
- **Mention related issues** — e.g., "Fixes #42" or "Related to #15"

Example PR:

```
Title: Add confidence tracking to review quiz

Description:
After each answer in REVIEW-PROMPT, ask learners "Sure / Guessing?" to track confidence levels. This helps identify which concepts they truly understand vs. luck.

Changes:
- Modified REVIEW-PROMPT.md step 6 (Scoring and feedback)
- Added confidence tracking question after each answer reveal
- Updated END OF SESSION section to show confidence trend
- Updated STUDY-GUIDE.md to explain confidence tracking

Testing:
- Tested with Claude Opus in Cowork (5 questions)
- Confidence tracked correctly; no crashes or parsing errors

Closes #28
```

## Code of Conduct

- **Be respectful** — disagreement is fine; disrespect is not
- **Assume good intent** — we're all here to help
- **Give credit** — acknowledge ideas and contributions from others
- **Focus on the work** — keep discussions technical and constructive

## Areas We Need Help With

- **More example configurations** — showcase bootcamp, self-paced, hybrid setups
- **Prompt testing** — run sessions with different CONFIG setups and report issues
- **Documentation improvements** — clearer explanations, tutorials, video guides
- **Bug reports** — find and report issues systematically
- **Feature ideas** — what would make CISSP prep easier?

## Questions?

- Check the **[README.md](README.md)** for quick answers
- Check **[STUDY-GUIDE.md](STUDY-GUIDE.md)** for CISSP details
- Open an issue if you're stuck or have questions

---

**Thank you for contributing!** Every issue, PR, and suggestion makes this kit better for the CISSP community.
