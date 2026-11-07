from pathlib import Path
import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from app.engine import evaluate
app=FastAPI(title='LLM-as-a-Judge & Golden Dataset Evaluation Framework',version='0.1.0')
SAMPLE=json.loads((Path(__file__).resolve().parent.parent/'data'/'sample.json').read_text())
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/sample')
def sample(): return SAMPLE
@app.get('/metrics')
def metrics(): return evaluate(SAMPLE)
@app.post('/evaluate')
def run_evaluation(cases:list[dict[str,Any]]): return evaluate(cases)
