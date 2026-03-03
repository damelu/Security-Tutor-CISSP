# Obsidian Integration Guide

This guide shows how to use Obsidian as a visual study companion alongside the CISSP Study Kit. Obsidian provides graph views, note linking, and quiz generation from your study notes.

## Prerequisites

- Obsidian installed (free, https://obsidian.md)
- This study kit repo cloned locally
- (Optional) Node.js if using quiz generator plugin

## Step 1 — Open or create your vault

If using the included vault structure: copy the `CISSP/` folder from this repo into your Obsidian vault.

If starting fresh: create a new vault, then copy the `CISSP/` folder in.

## Step 2 — Enable community plugins

1. Open Obsidian Settings (gear icon)
2. Navigate to Community Plugins
3. Turn OFF "Restricted Mode"
4. Click "Browse" to open the plugin browser

## Step 3 — Install recommended plugins

### Quiz Generator (by ECuiDev)
Generates quiz questions from your notes.

1. Search "quiz generator" in the plugin browser
2. Install and enable
3. The domain notes have `quiz: true` in frontmatter — the plugin reads this

### Dataview (by Michael Brenan)
Auto-generates tables from note metadata.

1. Search "dataview" in the plugin browser
2. Install and enable
3. Progress-Tracking.md uses dataview queries (optional — works as manual table too)

## Step 4 — Link your Wrong Answer Bank

Choose one of two options:

### Option A — Symlink (recommended, real-time sync)

**macOS / Linux:**
```bash
ln -s /path/to/cissp-study-kit/WRONG-ANSWER-BANK.md /path/to/obsidian-vault/CISSP/WRONG-ANSWER-BANK.md
```

**Windows (PowerShell as admin):**
```powershell
New-Item -ItemType SymbolicLink -Path "C:\vault\CISSP\WRONG-ANSWER-BANK.md" -Target "C:\kit\WRONG-ANSWER-BANK.md"
```

Both the kit and Obsidian see the same file. Changes from Claude sessions appear instantly in Obsidian.

### Option B — Manual copy

After each study session, copy WRONG-ANSWER-BANK.md into your vault's CISSP/ folder. Simple but requires remembering.

## Step 5 — Using the Quiz Generator plugin

1. Open any domain note (e.g., Domain-1-Overview.md)
2. Click the Quiz Generator icon in the sidebar (or use command palette: "Generate Quiz")
3. The plugin reads the note content and generates quiz questions
4. Answer questions in the Obsidian UI
5. For spaced repetition: pair with the "Spaced Repetition" plugin (optional)

## Step 6 — Graph view

Open Obsidian's Graph View to visualize domain connections. Domain notes link to each other via [[wikilinks]]. The graph shows which domains are most interconnected — useful for understanding cross-domain concepts.

## Step 7 — Daily workflow with Obsidian

1. Run your nightly study session in Cowork/IDE (DAILY-PROMPT.md)
2. After the session, open Obsidian
3. Check Progress-Tracking.md for updated stats
4. Use Quiz Generator on weak domains for extra practice
5. Review the Graph View to see domain relationships

## Vault Structure

```
Your Obsidian Vault/
├── CISSP/
│   ├── 01-Security-Risk-Management/
│   │   └── Domain-1-Overview.md
│   ├── 02-Asset-Security/
│   │   └── Domain-2-Overview.md
│   ├── ... (6 more domains)
│   ├── CISSP-Index.md
│   ├── Progress-Tracking.md
│   └── WRONG-ANSWER-BANK.md (symlinked)
├── Templates/
│   └── domain-note-template.md
```

## Tips

- Domain notes have YAML frontmatter with `quiz: true` — this tells the Quiz Generator plugin to include them
- The `difficulty` array in frontmatter helps you filter by tier
- Use Obsidian's search to find concepts across all domain notes
- Canvas mode: create a visual map of domain relationships
- Tags (#cissp, #domain1, etc.) make searching and filtering easy

## Without Plugins

Everything works without plugins — you just won't get auto-generated quizzes or auto-updating tables. The notes are standard markdown with wikilinks.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Quiz generator not finding notes | Make sure `quiz: true` is in the frontmatter |
| Dataview not rendering | Enable the plugin, then reload Obsidian |
| Symlink not working | Check file permissions; on macOS, make sure both paths are accessible |
| Wrong Answer Bank not updating | Check symlink points to correct path; use `ls -la` to verify |
