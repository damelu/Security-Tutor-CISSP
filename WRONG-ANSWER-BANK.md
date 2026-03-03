# Wrong Answer Bank

This file tracks every question you answer incorrectly across all study sessions. It's your personalized study guide—your weak areas accumulate here for targeted review.

**Important**: This file is auto-updated by DAILY-PROMPT.md and REVIEW-PROMPT.md. Don't delete old entries; they help identify patterns in your knowledge gaps.

---

## Summary

Domain counts update automatically as you study. Use this to see where your weak areas are at a glance.

| Domain | Wrong Answers | Accuracy |
|--------|---------------|----------|
| Security and Risk Management | 0 | — |
| Asset Security | 0 | — |
| Security Architecture and Engineering | 0 | — |
| Communication and Network Security | 0 | — |
| Identity and Access Management | 0 | — |
| Security Assessment and Testing | 0 | — |
| Security Operations | 0 | — |
| Software Development Security | 0 | — |
| **TOTAL** | **0** | **—** |

---

## Entries

Entries appear here as you study. Each wrong answer includes:

- **Question**: The full question text
- **Your Answer**: What you answered
- **Correct Answer**: The right answer
- **Domain**: Which CISSP domain it covers
- **Explanation**: Why the correct answer is right (2-3 sentences)
- **Memory Hook**: A vivid way to remember this concept
- **Attempts**: How many times you've seen this question
- **Last Reviewed**: When you last studied this concept
- **Source**: Where it came from (materials, transcript, Claude knowledge)
- **Status**: Active (still reviewing) or Mastered (you got it right 3x in a row)

---

## Template for New Entries

When the system adds a wrong answer, it will look like this:

```markdown
### Entry 1: [Descriptive title]

- **Question**: [Full question text]
- **Your Answer**: [A/B/C/D, or what you said]
- **Correct Answer**: [A/B/C/D, or correct answer]
- **Domain**: [Domain name]
- **Explanation**: [2-3 sentences explaining why the correct answer is right]
- **Memory Hook**: [Vivid way to remember this]
- **Attempts**: 1
- **Last Reviewed**: [Date]
- **Source**: [materials / transcript / Claude knowledge]
- **Status**: Active
```

---

## Example Entries (For Reference)

These are examples to show you the format. Your actual entries will replace these.

### Example 1: Least Privilege Principle

- **Question**: Which principle states that users should be granted only the minimum permissions necessary to perform their job functions?
- **Your Answer**: C (Defense in Depth)
- **Correct Answer**: B (Least Privilege)
- **Domain**: Security and Risk Management
- **Explanation**: Least Privilege is the security principle of giving users only what they NEED to do their job. Defense in Depth is about layering multiple security controls. Least Privilege is about minimizing access; Defense in Depth is about redundant protections.
- **Memory Hook**: "Least = Minimum. Give users the LEAST they need, not what they want. Don't trust them with extras."
- **Attempts**: 1
- **Last Reviewed**: 2026-03-03
- **Source**: Claude knowledge
- **Status**: Active

### Example 2: Risk Formula

- **Question**: In risk management, what does the formula Risk = Threat × Vulnerability × Asset Value represent?
- **Your Answer**: A (A method to calculate total company risk)
- **Correct Answer**: B (The relationship between threat, vulnerability, and impact)
- **Domain**: Security and Risk Management
- **Explanation**: Risk is a function of three factors: whether a threat exists, whether a vulnerability allows it to be exploited, and what the impact would be. All three must be present for risk to exist. If any is zero, risk is zero.
- **Memory Hook**: "Think of a locked door. You need: 1) a criminal (threat), 2) a broken lock (vulnerability), 3) something valuable inside (asset value). Miss one? No risk."
- **Attempts**: 1
- **Last Reviewed**: 2026-03-03
- **Source**: Claude knowledge
- **Status**: Active

### Example 3: AES Encryption

- **Question**: What is the key length of AES-256?
- **Your Answer**: D (128 bits)
- **Correct Answer**: A (256 bits)
- **Domain**: Security Architecture and Engineering
- **Explanation**: AES comes in three variants: AES-128 (128-bit keys), AES-192 (192-bit keys), and AES-256 (256-bit keys). The number in the name refers to key length, not block size. AES-256 is the strongest variant recommended for top-secret data.
- **Memory Hook**: "AES-256 = 256-bit keys. 256 is the GOLD STANDARD. Anything less is weaker. 'AES-256 for secrets!' Remember: bigger number = stronger encryption."
- **Attempts**: 2
- **Last Reviewed**: 2026-03-04
- **Source**: Claude knowledge
- **Status**: Active

---

## How This File Works

### Automatic Updates

Each time you run DAILY-PROMPT.md or REVIEW-PROMPT.md:

1. You answer questions
2. For each wrong answer, the system:
   - Adds it to this file (if new)
   - Updates the attempt count (if repeat)
   - Updates "Last Reviewed" date
   - Recalculates domain summary counts
3. The file is your living study guide

### Using Wrong Answers to Study

1. **Before next session**: Review your wrongs from the previous day
2. **During reviews**: Check which domains have the most entries—study those harder
3. **Weekly review quiz**: Weighted toward your weak domains (those with most wrongs)
4. **Spaced repetition**: As you review, the system marks answers as "Mastered" after 3 consecutive correct attempts

### Mastery Tracking

Once you answer a question correctly **3 times in a row**, it's marked "Mastered" and moved to a lower-review frequency. But it stays in the bank for long-term retention.

---

## Domain Focus

If you notice a domain has many entries, dedicate extra daily study to it:

| Domain | ISC2 Exam Weight | Tips If Weak |
|--------|---|---|
| Security and Risk Management | 15% | Focus on frameworks, risk formulas, governance |
| Asset Security | 10% | Data handling, classification, lifecycle |
| Security Architecture and Engineering | 12% | Cryptography, secure design principles |
| Communication and Network Security | 14% | Network protocols, secure communication, PKI |
| Identity and Access Management | 13% | Authentication methods, access control models |
| Security Assessment and Testing | 12% | Vulnerability assessment, penetration testing |
| Security Operations | 16% | Incident response, logging, monitoring (largest domain!) |
| Software Development Security | 8% | SDLC, secure coding, application security (smallest domain) |

---

## Tips for Using This Bank

1. **Review before study**: At the start of each session, skim yesterday's wrongs
2. **Focus on frequency**: If a domain appears 5+ times, prioritize it next week
3. **Memory hooks matter**: Read the memory hooks aloud 3 times for better retention
4. **Don't memorize; understand**: The goal is conceptual understanding, not rote memorization
5. **Spaced repetition**: The system shows you wrongs again at increasing intervals (1 day, 3 days, 1 week, 2 weeks)

---

## Resetting or Archiving

If you want to start fresh:

1. **Keep current entries** (for learning): Don't delete—they're valuable
2. **Archive old entries**: Copy this file to `notes/wrong-answer-bank-archived-[date].md` before your next study phase
3. **Start new**: Create a fresh WRONG-ANSWER-BANK.md for the next cycle

But generally, keeping all entries helps identify recurring misconceptions.

---

## Integration with Daily & Review Prompts

- **DAILY-PROMPT.md**: Reads this file to see your weak domains, adds new wrongs
- **REVIEW-PROMPT.md**: Uses this file to weight the 40-question review (more questions on weak domains)
- **CONFIG.md**: Tells the system your study settings; wrong answers stay independent of schedule

---

## Questions?

- **Why keep old wrong answers?** Pattern recognition—if you miss the same concept twice, that's where to focus
- **Can I add my own entries?** Yes! Use the template above. Manual entries help if you want to log wrongs from outside sources
- **Should I delete "Mastered" entries?** No. Keep them for long-term retention; they'll be reviewed less frequently
- **What if I have 50+ entries in one domain?** That's important feedback: your review quiz will heavily weight that domain, and you should spend extra time there daily

---

**Your wrong answer bank is your study roadmap.** Use it to identify weak spots, track improvement, and focus your effort where it matters most.

**Ready to start?** Go to DAILY-PROMPT.md to run your first study session!
