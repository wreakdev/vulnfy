# Vulnfy

**Vulnfy** is a lightweight, cross-platform dependency and container vulnerability scanner written in Python. It automatically detects project configuration/lock files across multiple languages and ecosystems, queries the OSV (Open Source Vulnerabilities) API, and generates a structured JSON vulnerability report.

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


## Installation
```bash
curl -sSL https://github.com/wreakdev/vulnfy/blob/main/vulnfy_setup.sh | bash
```

## Usage
There is no arguments for now.
```bash
vulnfy
```