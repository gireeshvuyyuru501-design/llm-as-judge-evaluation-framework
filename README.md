# LLM-as-a-Judge & Golden Dataset Evaluation Framework

**Portfolio MVP — offline, reproducible demonstration.**

Offline lexical precision, recall and F1 provide a reproducible baseline. A real LLM-as-a-judge integration is NOT included; human review queue is based on F1 threshold.

## Features
- FastAPI endpoints: `/health`, `/sample`, `/metrics`, `/evaluate`
- Streamlit dashboard with overview, interactive evaluation and sample dataset
- Automated pytest suite and GitHub Actions CI
- No paid API keys required

## Quick start (Windows PowerShell)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```
In a **second** terminal in the same project directory (with virtual environment activated):
```powershell
python -m streamlit run streamlit_app.py
```
Open http://localhost:8501 and http://127.0.0.1:8000/docs.

**Important:** Stop other projects using port 8000 before starting this one.

## API example
```powershell
Invoke-RestMethod http://127.0.0.1:8000/metrics
```

## Scope
The demo uses sample data and deterministic evaluation; it does not make real LLM calls or claim production readiness. Replace the sample cases and add provider integrations before production use.

## Portfolio website

[Project overview on GitHub Pages](https://gireeshvuyyuru501-design.github.io/llm-as-judge-evaluation-framework/) (static landing page; run API and Streamlit locally).

[MIT License](LICENSE) | [Screenshots](screenshots/) | [Demo videos](demo/)

**Scope:** MVP: deterministic lexical scoring, not a live LLM-as-a-judge.

