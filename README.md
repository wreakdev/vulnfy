# Vulnfy
![vulnfy](https://github.com/wreakdev/vulnfy/blob/main/vulnfy.png)

---

**Vulnfy** is a lightweight, cross-platform dependency and container vulnerability scanner written in Python. It automatically detects project configuration/lock files across multiple languages and ecosystems, queries the OSV (Open Source Vulnerabilities) API, and generates a structured JSON vulnerability report.

---

## Features
- **Multi-Ecosystem Support:** Scans dependencies for Python, Node.js, Go, PHP, Rust, and container base images.
- **Batch OSV API Integration:** Efficiently checks packages in bulk using the OSV batch query API.
- **Automatic Dependency Resolution:** Automatically installs missing requirements (requests, colorama, PyYAML) on first run.
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