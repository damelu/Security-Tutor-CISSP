"""
CISSP Study Kit - Flask REST API Server
Reads/writes markdown files (single source of truth)
Runs locally only - no authentication required
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
import yaml
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Config
REPO_ROOT = Path(__file__).parent.parent
MARKDOWN_DIR = REPO_ROOT
PORT = int(os.environ.get('PORT', 5000))

# ============================================================================
# MARKDOWN PARSERS
# ============================================================================

def parse_config():
    """Parse CONFIG.md YAML blocks into a config dict."""
    config_file = MARKDOWN_DIR / 'CONFIG.md'
    if not config_file.exists():
        return get_default_config()

    try:
        content = config_file.read_text()
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)

        config = {}
        for block in yaml_blocks:
            try:
                parsed = yaml.safe_load(block)
                if isinstance(parsed, dict):
                    config.update(parsed)
            except yaml.YAMLError:
                continue

        return config if config else get_default_config()
    except Exception as e:
        print(f"Error parsing CONFIG.md: {e}")
        return get_default_config()

def get_default_config():
    """Return sensible defaults."""
    return {
        'schedule_mode': 'adaptive',
        'difficulty_mode': 'progressive',
        'difficulty_distribution': [25, 50, 25],  # easy, medium, hard
        'daily_quiz_questions': 10,
        'generate_audio': False,
        'weak_domain_difficulty_boost': 1.5,
    }

def parse_wrong_answer_bank():
    """Parse WRONG-ANSWER-BANK.md entries and summary."""
    bank_file = MARKDOWN_DIR / 'WRONG-ANSWER-BANK.md'
    if not bank_file.exists():
        return {'entries': [], 'summary': {}}

    try:
        content = bank_file.read_text()
        entries = []

        # Parse entries: ### Entry N: [title]
        entry_pattern = r'### Entry \d+: (.+?)\n(.*?)(?=###|$)'
        for match in re.finditer(entry_pattern, content, re.DOTALL):
            title = match.group(1).strip()
            body = match.group(2).strip()

            entry = {'title': title}

            # Extract fields with regex
            fields = ['Question', 'Your Answer', 'Correct Answer', 'Domain',
                     'Difficulty', 'Explanation', 'Memory Hook', 'Attempts',
                     'Last Reviewed', 'Source', 'Status']

            for field in fields:
                pattern = f'\\*\\*{field}\\*\\*: (.+?)(?=\\n\\*\\*|$)'
                field_match = re.search(pattern, body, re.DOTALL)
                if field_match:
                    entry[field.lower().replace(' ', '_')] = field_match.group(1).strip()

            entries.append(entry)

        return {'entries': entries, 'summary': parse_summary_table(content)}
    except Exception as e:
        print(f"Error parsing WRONG-ANSWER-BANK.md: {e}")
        return {'entries': [], 'summary': {}}

def parse_summary_table(content):
    """Extract domain summary from markdown table."""
    summary = {}
    table_pattern = r'\| Domain \| .+?\n\|[-\s|:]+\n(.*?)(?=\n\n|$)'
    match = re.search(table_pattern, content, re.DOTALL)

    if match:
        rows = match.group(1).strip().split('\n')
        for row in rows:
            parts = [p.strip() for p in row.split('|')[1:-1]]
            if len(parts) >= 6 and parts[0] and parts[0] != 'Domain':
                try:
                    summary[parts[0]] = {
                        'wrong_count': int(parts[1]),
                        'associate': int(parts[2]),
                        'professional': int(parts[3]),
                        'expert': int(parts[4]),
                        'accuracy': float(parts[5].rstrip('%')) / 100,
                    }
                except (ValueError, IndexError):
                    pass

    return summary

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/')
def serve_index():
    """Serve index.html"""
    return send_from_directory('.', 'index.html')

@app.route('/api/config')
def api_config():
    """Return parsed CONFIG.md as JSON."""
    config = parse_config()
    return jsonify(config)

@app.route('/api/questions')
def api_questions():
    """Return questions from questions.json (filtered by domain/difficulty)."""
    questions_file = MARKDOWN_DIR / 'questions.json'
    if not questions_file.exists():
        return jsonify([])

    try:
        questions = json.loads(questions_file.read_text())

        # Filter by query params
        domain = request.args.get('domain')
        difficulty = request.args.get('difficulty')

        if domain:
            questions = [q for q in questions if q.get('domain') == domain]
        if difficulty:
            questions = [q for q in questions if q.get('difficulty') == difficulty]

        return jsonify(questions)
    except Exception as e:
        print(f"Error reading questions.json: {e}")
        return jsonify([])

@app.route('/api/bank')
def api_bank():
    """Return parsed WRONG-ANSWER-BANK.md entries + summary."""
    bank = parse_wrong_answer_bank()
    return jsonify(bank)

@app.route('/api/bank/add', methods=['POST'])
def api_bank_add():
    """Add wrong answer entry (section-based overwrite for today)."""
    try:
        data = request.get_json()
        bank_file = MARKDOWN_DIR / 'WRONG-ANSWER-BANK.md'

        # Get or create bank content
        if bank_file.exists():
            content = bank_file.read_text()
        else:
            content = "# Wrong Answer Bank\n\n"

        # Get today's date section header
        today = datetime.now().strftime('%Y-%m-%d')
        session_header = f'## {today} Session'

        # Find and remove today's section
        session_pattern = f'## {today} Session.*?(?=## \\d{{4}}-\\d{{2}}-\\d{{2}}|$)'
        content = re.sub(session_pattern, '', content, flags=re.DOTALL).strip()

        # Build new entries
        new_entries = []
        for i, entry in enumerate(data.get('entries', []), 1):
            entry_text = f"### Entry {i}: {entry.get('title', 'Untitled')}\n\n"
            for key, value in entry.items():
                if key != 'title':
                    field_name = ' '.join(w.capitalize() for w in key.split('_'))
                    entry_text += f"**{field_name}**: {value}\n\n"
            new_entries.append(entry_text)

        # Add new session section
        new_section = f"\n\n{session_header}\n\n" + "".join(new_entries)
        content += new_section

        bank_file.write_text(content)
        return jsonify({'status': 'success', 'date': today})

    except Exception as e:
        print(f"Error adding to bank: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/stats')
def api_stats():
    """Calculate domain scores, difficulty breakdown, progress metrics."""
    bank = parse_wrong_answer_bank()
    entries = bank.get('entries', [])

    stats = {
        'total_wrongs': len(entries),
        'by_domain': {},
        'by_difficulty': {},
        'last_reviewed': None,
    }

    for entry in entries:
        domain = entry.get('domain', 'Unknown')
        difficulty = entry.get('difficulty', 'Unknown')

        if domain not in stats['by_domain']:
            stats['by_domain'][domain] = 0
        stats['by_domain'][domain] += 1

        if difficulty not in stats['by_difficulty']:
            stats['by_difficulty'][difficulty] = 0
        stats['by_difficulty'][difficulty] += 1

        # Track most recent review
        reviewed = entry.get('last_reviewed')
        if reviewed and (not stats['last_reviewed'] or reviewed > stats['last_reviewed']):
            stats['last_reviewed'] = reviewed

    return jsonify(stats)

@app.route('/api/settings', methods=['POST'])
def api_settings():
    """Update CONFIG.md settings."""
    try:
        data = request.get_json()
        config = parse_config()
        config.update(data)

        config_file = MARKDOWN_DIR / 'CONFIG.md'
        yaml_str = yaml.dump(config, default_flow_style=False)
        new_content = f"# CISSP Study Kit Configuration\n\n```yaml\n{yaml_str}```\n"

        config_file.write_text(new_content)
        return jsonify({'status': 'success', 'config': config})

    except Exception as e:
        print(f"Error updating settings: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/review-distribution')
def api_review_distribution():
    """Calculate 40-question review distribution using ISC2 weights + bank weakness."""
    config = parse_config()
    bank = parse_wrong_answer_bank()

    # ISC2 domain weights
    isc2_weights = {
        'SRM': 0.15,  # Security & Risk Management
        'AS': 0.10,   # Asset Security
        'SAE': 0.12,  # Security Architecture & Engineering
        'CNS': 0.14,  # Communication & Network Security
        'IAM': 0.13,  # Identity & Access Management
        'SAT': 0.12,  # Security Assessment & Testing
        'SO': 0.16,   # Security Operations
        'SDS': 0.08,  # Software Development Security
    }

    # Count wrongs per domain
    wrong_counts = {}
    for entry in bank.get('entries', []):
        domain = entry.get('domain', 'Unknown')
        wrong_counts[domain] = wrong_counts.get(domain, 0) + 1

    # Apply weakness boost/reduction
    boost_factor = config.get('weak_domain_difficulty_boost', 1.5)
    adjusted_weights = {}

    for domain, base_weight in isc2_weights.items():
        wrong_count = wrong_counts.get(domain, 0)
        if wrong_count >= 3:
            adjusted_weights[domain] = base_weight * boost_factor
        elif wrong_count == 0:
            adjusted_weights[domain] = base_weight * 0.8
        else:
            adjusted_weights[domain] = base_weight

    # Normalize to 100%
    total = sum(adjusted_weights.values())
    normalized = {d: (w / total) for d, w in adjusted_weights.items()}

    # Distribute 40 questions
    distribution = {d: max(1, round(w * 40)) for d, w in normalized.items()}

    # Adjust difficulty for strong/weak domains
    difficulty_boost = {}
    for domain in distribution.keys():
        accuracy = 1.0 - (wrong_counts.get(domain, 0) / 40)  # Simple estimate
        if accuracy >= 0.8:
            difficulty_boost[domain] = 'professional'  # Push up one tier
        elif accuracy < 0.7:
            difficulty_boost[domain] = 'associate'     # Keep or drop
        else:
            difficulty_boost[domain] = 'professional'   # Normal

    return jsonify({
        'distribution': distribution,
        'difficulty_adjustment': difficulty_boost,
        'total_questions': sum(distribution.values()),
        'weights': normalized,
    })

# ============================================================================
# SERVER STARTUP
# ============================================================================

if __name__ == '__main__':
    print(f"CISSP Study Kit Server starting...")
    print(f"Repo root: {REPO_ROOT}")
    print(f"Markdown dir: {MARKDOWN_DIR}")
    print(f"Serving on http://0.0.0.0:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
