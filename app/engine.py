import re

def tokens(s): return set(re.findall(r"[a-z0-9]+",s.lower()))

def score_case(case):
    """Offline baseline, NOT an LLM judge."""
    expected=tokens(case['reference']); actual=tokens(case['answer'])
    precision=len(expected & actual)/len(actual) if actual else 0
    recall=len(expected & actual)/len(expected) if expected else 0
    f1=2*precision*recall/(precision+recall) if precision+recall else 0
    return {'id':case['id'],'precision':round(precision,3),'recall':round(recall,3),'f1':round(f1,3),'needs_human_review':f1<0.65,'judge':'lexical_baseline'}

def evaluate(cases):
    scores=[score_case(c) for c in cases]
    return {'count':len(scores),'mean_f1':round(sum(x['f1'] for x in scores)/len(scores),3) if scores else 0,'cases':scores}
