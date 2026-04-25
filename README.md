# Polymarket Starter (Python)

Small personal project to explore Polymarket data via public APIs.

## Features

- List active markets via Gamma API.
- Fetch a market by slug.
- Pull order book + last trade price for the first outcome token.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venvScriptsactivate on Windows
pip install -r requirements.txt
cp .env.example .env  # optional