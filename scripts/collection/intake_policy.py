"""Maintainer-owned Star exceptions; never derive approval from upstream or issues."""
import json
from datetime import datetime

def star_threshold_exempt(root, repository):
    path = root / 'data/project-intake-overrides.json'
    if not path.exists():
        return False
    entry = json.loads(path.read_text()).get(repository.removeprefix('https://github.com/').lower())
    if entry is None:
        return False
    if entry.get('starThresholdExempt') is not True or entry.get('approvedBy') != 'site-owner' or not entry.get('reason') or not entry.get('approvedAt'):
        raise ValueError('Star exemption needs explicit site-owner approval, date and reason')
    datetime.fromisoformat(entry['approvedAt'].replace('Z', '+00:00'))
    return True
