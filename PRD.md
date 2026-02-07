# Pipeline Graph Inspector — PRD

## Problem
Pipelines grow organically. A tiny typo can turn into a broken run. You want a quick validator + visualization before execution.

## Goals
- Accept a simple JSON pipeline definition: steps + dependencies.
- Validate: missing deps, cycles, unreachable steps.
- Export a Mermaid graph.

## Non-goals
- Executing the pipeline.
- Supporting every workflow DSL.

## API
- `POST /api/pipeline/inspect`

## UX (Streamlit)
- Paste JSON pipeline.
- View lint results + Mermaid output.

## Sources
- Hugging Face — Daggr: https://huggingface.co/blog/daggr
