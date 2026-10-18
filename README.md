[![FreeLLM.net](https://github.com/open-free-llm-api/free-llm-models-python/raw/main/og-image.jpg)](https://freellm.net)

# free-llm-models

[![PyPI version](https://img.shields.io/pypi/v/free-llm-models.svg)](https://pypi.org/project/free-llm-models/)
[![PyPI downloads](https://img.shields.io/pypi/dm/free-llm-models.svg)](https://pypi.org/project/free-llm-models/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/open-free-llm-api/free-llm-models-python.svg)](https://github.com/open-free-llm-api/free-llm-models-python/stargazers)

A curated, machine-readable directory of **537+ free LLM APIs and models** from 30+ providers. Query it from your terminal or import it into your Python projects.

Data is synced daily from [FreeLLM](https://freellm.net) — the free LLM API directory with live playground. Browse the full interactive catalog at [freellm.net](https://freellm.net).

> **JavaScript user?** There's an npm twin: [`free-llm-models` on npm](https://www.npmjs.com/package/free-llm-models) · [GitHub](https://github.com/open-free-llm-api/free-llm-models)

## Installation

```bash
pip install free-llm-models
```

## CLI Usage

```bash
# List free models (default 20, use --limit for more)
free-llm-models list --limit 10

# Filter by provider
free-llm-models list --provider opencode

# Search by keyword
free-llm-models search claude

# Show model details
free-llm-models info kimi-k2-7-code

# List all providers with model counts
free-llm-models providers

# Compare two models side by side
free-llm-models compare kimi-k2-7-code claude-fable-5

# Get a random recommendation
free-llm-models random

# Machine-readable JSON output (great for scripts)
free-llm-models search gpt --json
```

## Python API

```python
import free_llm_models as flm

# Search models
results = flm.search('claude')

# Get a specific model
model = flm.get('kimi-k2-7-code')
print(model['provider'])  # 'opencode'

# List providers
providers = flm.providers()

# Filter by provider
models = flm.by_provider('opencode')

# Get dataset metadata
meta = flm.meta()  # {'updated', 'source', 'count'}
```

## Data

| Field | Description |
|-------|-------------|
| `id` | Unique model identifier |
| `name` | Human-readable model name |
| `provider` | Provider name (e.g. `opencode`, `google-gemini`) |
| `supportsTools` | Whether the model supports function calling |
| `supportsJson` | Whether the model supports JSON mode |
| `released` | Release date (ISO 8601) |

- **537 models** across 30+ providers
- Updated: 2026-10-18
- Full interactive directory with playground: [https://freellm.net](https://freellm.net)

## Relationship with awesome-freellm-apis

This package is the machine-readable companion to [awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) (the curated awesome list, 4.4k+ stars).

| | awesome-freellm-apis | free-llm-models |
|---|---|---|
| Format | Human-readable awesome list | JSON data + CLI + API |
| Use case | Browse & compare in browser | Query from terminal / code |
| Data source | Same freellm.net dataset | Same freellm.net dataset |

Both are maintained by the [open-free-llm-api](https://github.com/open-free-llm-api) organization and synced from [freellm.net](https://freellm.net).

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

MIT © [MyToolster](https://freellm.net)
