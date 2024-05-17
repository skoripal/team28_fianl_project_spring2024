import streamlit as st
import json
import requests

st.title('Predict Charges')

# Load sidebar options from a JSON file
with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        min_val, max_val = value
        current_value = (min_val + max_val) // 2
        options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)

# Display the current options selected by the user
st.write(options)

# When the user clicks the 'Predict' button
if st.button('Predict'):
    # Prepare the payload for the POST request
    payload = json.dumps(options)
    try:
        # Make a POST request to the API
        response = requests.post(
            url="http://45.55.203.144:3333/docs/",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        response_data = response.json()

        # Check if 'prediction' is in the response and handle accordingly
        if 'prediction' in response_data:
            prediction = response_data['prediction']
            st.write(f'The predicted Policy Charges is: ${prediction:,}')
        else:
            st.error('No prediction found in the response.')
    except Exception as e:
        st.error(f"Failed to retrieve prediction. Error: {e}")
