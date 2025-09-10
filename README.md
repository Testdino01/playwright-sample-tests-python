# Ecommerce-demo-store
Automated end-to-end tests for Ecommerce Demo Store using [Playwright](https://playwright.dev/) and Python.

---

## Project Structure

- `pages/` — Page Object Models (Python classes)
- `tests/` — Test specifications (`pytest` test files)
- `playwright-report/` — HTML and JSON test reports
- `.github/workflows/test.yml` — CI/CD pipeline (GitHub Actions)
- `conftest.py` — Pytest and Playwright fixtures/configuration

---

## Prerequisites

- [Python](https://www.python.org/) 3.9+
- [pip](https://pip.pypa.io/en/stable/)

---

## Installation

```sh
python -m pip install --upgrade pip
pip install pytest pytest-playwright pytest-html pytest-json-report python-dotenv
python -m playwright install
```

---

## Local Test Execution

Run all tests:
```sh
pytest
```

Run tests with HTML and JSON reports:
```sh
pytest --html=playwright-report/report.html --json-report --json-report-file=playwright-report/report.json
```

---

## Viewing Reports

Open the HTML report after test run:
```sh
open playwright-report/report.html
```
*(On Windows use `start`, on Linux use `xdg-open`)*

---

## Testdino Integration

[Testdino](https://testdino.com/) enables cloud-based Playwright reporting.

After your tests complete and the report is generated in `playwright-report`, upload it to Testdino:

```sh
npx --yes tdpw ./playwright-report --token="your-token" --upload-html
```

Replace `"your-token"` with your own Testdino API key.

See all available commands:
```sh
npx tdpw --help
```

---

## CI/CD Pipeline Integration

### GitHub Actions

Add the following step to your workflow after tests and report generation:

```yaml
- name: Send Testdino report
  run: |
    npx --yes tdpw ./playwright-report --token="your-token" --upload-html
```

Ensure your API key is correctly placed in the command.

---

## Continuous Integration

Automated test runs and report merging are configured in `.github/workflows/test.yml`.

---

## Contributing

Pull requests and issues are welcome!

---

## License

MIT
