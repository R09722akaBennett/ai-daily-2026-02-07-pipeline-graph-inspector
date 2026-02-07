from __future__ import annotations

import json
import streamlit as st

from app.web.app_factory import api_post

st.set_page_config(page_title='Pipeline Graph Inspector', layout='wide')

st.title('Pipeline Graph Inspector')
st.caption('Validate a tiny pipeline JSON and export Mermaid.')

sample = {
  'steps': [
    {'id': 'fetch', 'deps': []},
    {'id': 'transform', 'deps': ['fetch']},
    {'id': 'train', 'deps': ['transform']},
    {'id': 'report', 'deps': ['train']},
  ]
}

raw = st.text_area('Pipeline JSON', value=json.dumps(sample, indent=2), height=240)

if st.button('Inspect'):
    payload = json.loads(raw)
    res = api_post('/api/pipeline/inspect', payload)
    if res['ok']:
        st.success('OK')
    else:
        st.error('Issues found')
        st.write(res['errors'])

    st.subheader('Topological order')
    st.code(' -> '.join(res['topo_order']), language='text')

    st.subheader('Mermaid')
    st.code(res['mermaid'], language='text')
