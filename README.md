# Pipeline Graph Inspector

Validate and visualize simple pipeline definitions as a DAG, with linting and Mermaid export.

## Inspiration / Sources

- https://huggingface.co/blog/daggr

## Architecture

- FastAPI backend: `app/` (app factory + routers + services)
- Streamlit UI: `app/web/streamlit_app.py`

## Run (dev)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
```

Terminal A (API):

```bash
./scripts/dev_api.sh
```

Terminal B (UI):

```bash
./scripts/dev_ui.sh
```

## Smoke test

```bash
curl -s http://127.0.0.1:8000/api/health | python3 -m json.tool
```
