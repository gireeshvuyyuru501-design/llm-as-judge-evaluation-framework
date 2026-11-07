from app.engine import evaluate
from app.main import SAMPLE
from fastapi.testclient import TestClient
from app.main import app

def test_evaluation_count():
    assert evaluate(SAMPLE)['count']==len(SAMPLE)

def test_empty_cases():
    assert evaluate([])['count']==0

def test_health():
    assert TestClient(app).get('/health').json()=={'status':'ok'}

def test_api_evaluate():
    r=TestClient(app).post('/evaluate',json=SAMPLE)
    assert r.status_code==200
    assert r.json()['count']==len(SAMPLE)
