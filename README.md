# Vulnfy
![vulnfy](https://github.com/wreakdev/vulnfy/blob/main/vulnfy.png)

---

**Vulnfy** is a lightweight, cross-platform dependency and container vulnerability scanner written in Python. It automatically detects project configuration/lock files across multiple languages and ecosystems, queries the OSV (Open Source Vulnerabilities) API, and generates a structured JSON vulnerability report.

---

## Features
- **Multi-Ecosystem Support:** Scans dependencies for Python, Node.js, Go, PHP, Rust, and container base images.
- **Batch OSV API Integration:** Efficiently checks packages in bulk using the OSV batch query API.
- **Instant Notifications:** Automatically sends vulnerability alerts to Discord or Telegram based on your configuration.
- **CI/CD Ready:** Exits with a non-zero status code (`sys.exit(1)`) if vulnerabilities are found, making it ideal for automation.
- **Automatic Dependency Resolution:** Automatically installs missing requirements (`requests`, `colorama`, `PyYAML`) on first run.
- **Structured Output:** Exports all discovered vulnerabilities and associated CVEs into a clean JSON report.

## Supports
| Lang          | File          |
| ------------- |:-------------:|
| Python        | requirements.txt, pyproject.toml |
| NPM           | package.json, package-lock.json  |
| Go            | go.mod      |
| PHP           | composer.lock |
| Rust          | Cargo.lock, Cargo.toml |
| Docker        | Dockerfile, docker-compose.yml | 

## Report example
This is a Python example, but some results do not have an assigned CVE.
```json
{
    "ecosystem": "PyPI",
    "package": "jinja2",
    "vulnerability_id": "PYSEC-2026-1474",
    "cve": "CVE-2024-34064",
    "severity": "CVSS:3.1",
    "published": "2026-07-07",
    "description": "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter"
},
```

## Configuration (`config.yaml`)
Create a `config.yaml` file in the root directory to enable notifications:
```yaml
notifications:
  discord:
    enabled: true   # Set to true to enable Discord alerts
  telegram:
    enabled: false  # Set to true to enable Telegram alerts
```

## Environment Variables (`.env`)
For security reasons, API tokens and webhooks are loaded from environment variables. Copy `.env.example` to `.env` and fill in your credentials:
```env
# Can be used in Github Actions
# --- Discord ---
DISCORD_WEBHOOK_URL=
# --- Telegram ---
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

## CI/CD  Integration (Github Actions)
1. Create a `vulnfy.yaml` file in your repository root (as shown above).
2. Add your tokens to your repository **Settings -> Secret and variables -> Actions** (`DISCORD_WEBHOOK_URL`, etc..).
3. Create a workflow file in your project at `.github/workflows/scan.yaml`:
```yml
name: Vulnfy Security Scan

on:
  push:
    branches: [ main ]

jobs:
  vulnfy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Run Vulnfy Scanner
        uses: wreakdev/vulnfy@main
        env:
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
```

## Installation
```bash
curl -sSL https://github.com/wreakdev/vulnfy/blob/main/vulnfy_setup.sh | bash
```

## Usage
There is no arguments for now.
```bash
vulnfy
```
Find the project you want to check and launch it.