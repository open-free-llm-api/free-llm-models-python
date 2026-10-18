"""free-llm-models: query 500+ free LLM APIs from Python."""
import json
import os
import random as _random

_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'models.json')

with open(_DATA_PATH) as f:
    _data = json.load(f)

MODELS = _data['models']


def all():
    """Return all models."""
    return MODELS


def search(keyword):
    """Search models by name, id, or provider."""
    kw = keyword.lower()
    return [m for m in MODELS
            if kw in m['name'].lower()
            or kw in m['id'].lower()
            or kw in m['provider'].lower()]


def get(id_or_name):
    """Get a single model by id or name."""
    kw = id_or_name.lower()
    for m in MODELS:
        if m['id'].lower() == kw or m['name'].lower() == kw:
            return m
    return None


def providers():
    """Return list of providers with model counts, sorted desc."""
    counts = {}
    for m in MODELS:
        counts[m['provider']] = counts.get(m['provider'], 0) + 1
    return sorted(
        [{'name': k, 'count': v} for k, v in counts.items()],
        key=lambda x: -x['count']
    )


def by_provider(provider):
    """Filter models by provider name."""
    kw = provider.lower()
    return [m for m in MODELS if m['provider'].lower() == kw]


def random():
    """Return a random model."""
    return _random.choice(MODELS)


def meta():
    """Return dataset metadata."""
    return {
        'updated': _data['updated'],
        'source': _data['source'],
        'count': _data['count'],
    }
