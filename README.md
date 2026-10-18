# free-llm-models (Python)

A curated, machine-readable list of **500+ free LLM APIs and models** from 30+ providers — queryable from Python or your terminal.

Data is synced from [FreeLLM](https://freellm.net), the free LLM API directory. Browse the full catalog at [freellm.net](https://freellm.net).

> **JavaScript user?** There's an npm twin: [`free-llm-models` on npm](https://www.npmjs.com/package/free-llm-models) · [GitHub](https://github.com/open-free-llm-api/free-llm-models)

## Install

```bash
pip install free-llm-models
```

## CLI Usage

```bash
# List free models
free-llm-models list --limit 10

# Filter by provider
free-llm-models list --provider opencode

# Search
free-llm-models search claude

# Model details
free-llm-models info kimi-k2-7-code

# All providers
free-llm-models providers

# Compare two models
free-llm-models compare kimi-k2-7-code claude-fable-5

# Random pick
free-llm-models random

# JSON output
free-llm-models search gpt --json
```

## Python API

```python
import free_llm_models as flm

flm.search('claude')       # [...matches]
flm.get('kimi-k2-7-code')  # { 'id', 'name', 'provider', ... }
flm.providers()            # [{'name', 'count'}]
flm.random()               # one random model
flm.meta()                 # {'updated', 'source', 'count'}
```

## Data

- **537 models** across 30+ providers (updated 2026-10-18)
- Full interactive directory: [https://freellm.net](https://freellm.net)

## License

MIT

## Relationship with awesome-freellm-apis

This package is the machine-readable companion to [awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) (the curated awesome list, 4.4k+ stars).

| | awesome-freellm-apis | free-llm-models |
|---|---|---|
| Format | Human-readable awesome list | JSON data + CLI + API |
| Use case | Browse & compare in browser | Query from terminal / code |
| Data source | Same freellm.net dataset | Same freellm.net dataset |

Both are maintained by the [open-free-llm-api](https://github.com/open-free-llm-api) org and synced from [freellm.net](https://freellm.net).
