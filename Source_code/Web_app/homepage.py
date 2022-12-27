#Used to create a Streamlit web app

import streamlit as st

st.set_page_config(
    page_title= "Text Classification Web App"
)



def train_page():
    st.markdown("# Train the BERT Model 🎈")
    st.sidebar.markdown("# Train BERT Model 🎈")

def test_page():
    st.markdown("# Test the BERT Model ❄️")
    st.sidebar.markdown("# Test BERT Model ❄️")

    input_text = st.text_input('Please type in your views: ')
    #st.write(input_text)

page_names_to_funcs = {
    "Train the BERT Model !!": train_page,
    "Test the BERT Model !!": test_page,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()