import streamlit as st
import json
import requests

st.title('Predict Charges')


with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        min_val, max_val = value
        current_value = ( min_val + max_val ) // 2
        options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)


st.write(options)

if st.button('Predict'): 
    # payload = json.dumps({'inputs': options})
    # response = requests.post(
    #     url=f"http://159.203.68.179:5001/invocations",
    #     data=payload,
    #     headers={"Content-Type": "application/json"},
    # )

    payload = json.dumps(options)
    response = requests.post(
        url=f"http://45.55.203.144:3333/docs/",
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    response = response.json()
    prediction = response.get('prediction')
    st.write(f'The predicted Policy Charges is: ${prediction:}')
