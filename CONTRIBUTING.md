# Contributing to free-llm-models

Thank you for your interest in contributing! This document outlines the process for contributing to this project.

## How to Contribute

### Reporting Issues

- Check existing [issues](https://github.com/open-free-llm-api/free-llm-models-python/issues) first
- Include the model name/ID and expected vs actual behavior
- For data issues (wrong provider, outdated info), mention the source

### Updating Model Data

Model data lives in `data/models.json` and is synced from [freellm.net](https://freellm.net). If you notice outdated information:

1. Verify against the provider's official documentation
2. Open an issue describing the discrepancy
3. Data updates are typically batched with the daily sync

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test locally:
   ```bash
   python -m free_llm_models.cli list --limit 5
   python -m free_llm_models.cli search <keyword>
   ```
5. Commit with a clear message
6. Push and open a Pull Request

### CLI Changes

When adding new CLI commands:
- Update `bin/cli.js`
- Add `--json` output support
- Update this README's CLI Usage section
- Keep output format consistent with existing commands

## Code Style

- Use 2-space indentation
- CommonJS modules (`require`/`module.exports`)
- No external dependencies for the core library

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
