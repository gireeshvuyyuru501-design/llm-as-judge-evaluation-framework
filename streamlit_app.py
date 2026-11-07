import streamlit as st
import requests
import pandas as pd
st.set_page_config(page_title='LLM-as-a-Judge & Golden Dataset Evaluation Framework',page_icon='📊',layout='wide')
st.title('LLM-as-a-Judge & Golden Dataset Evaluation Framework')
st.caption('Demo dashboard • FastAPI backend • sample data')
api=st.sidebar.text_input('FastAPI URL','http://127.0.0.1:8000').rstrip('/')
def get(path):
    try:
        r=requests.get(api+path,timeout=5);r.raise_for_status();return r.json()
    except requests.RequestException as e:st.error(f'Backend unavailable: {e}');return None
health=get('/health')
if health:
    st.sidebar.success("Backend online")
else:
    st.sidebar.warning("Start FastAPI first")
t1,t2,t3=st.tabs(['📊 Overview','🧪 Run evaluation','📁 Sample data'])
with t1:
    metrics=get('/metrics')
    if metrics:
        cols=st.columns(min(4,len(metrics)))
        for col,(k,v) in zip(cols,metrics.items()):
            if isinstance(v,(int,float)):col.metric(k.replace('_',' ').title(),v)
        st.json(metrics)
with t2:
    st.write('Edit JSON cases and evaluate against the backend.')
    initial=get('/sample') or []
    raw=st.text_area('Cases (JSON list)',value=__import__('json').dumps(initial,indent=2),height=320)
    if st.button('Run evaluation',type='primary'):
        try:
            cases=__import__('json').loads(raw)
            if not isinstance(cases,list):st.error('Input must be a JSON list')
            else:
                r=requests.post(api+'/evaluate',json=cases,timeout=10)
                if r.ok:st.json(r.json())
                else:st.error(f'HTTP {r.status_code}: {r.text}')
        except (ValueError,requests.RequestException) as e:st.error(str(e))
with t3:
    cases=get('/sample')
    if cases:st.dataframe(pd.DataFrame(cases),use_container_width=True)
