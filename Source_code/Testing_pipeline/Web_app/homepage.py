#Used to create a Streamlit web app


from pathlib import Path
import sys

import streamlit as st

sys.path.append("C:\\Users\\Hardik\\PycharmProjects\\Text_Classification_using_BERT")

import streamlit as st
import Config_Files.testing_pipeline_config as config

from Source_code.Testing_pipeline.prediction import Prediction

from Source_code.Testing_pipeline.Load_model import load_model

st.set_page_config(
        page_title= "Text Classification Web App"
    )

@st.cache(suppress_st_warning=True)
def load_downloaded_model():
    load_model()

load_downloaded_model()


if __name__ == '__main__':



    def train_page():
        st.markdown("# Train the BERT Model 🎈")
        st.sidebar.markdown("# Train BERT Model 🎈")

    def test_page():
        st.markdown("# Test the BERT Model ❄️")
        st.sidebar.markdown("# Test BERT Model ❄️")

        input_text = st.text_input('Please type in your views: ')

        #------ Prediction Calls starts from here---

        print('Running the test bert model tab')

        try:
            pred_obj = Prediction()
            print("Input Text: {}".format(input_text))
            output_index, output_prob = pred_obj.prediction_values(input_text)
            print("Output Index is: ", output_index)
            print("Output Probability is: ", output_prob)

            st.write('Sentiment of the input text is: {} with probablity: {}'.format(config.classes['classification_label'][output_index], output_prob) )

            print("Prediction has been generated")

        except Exception as e:
            print(e)



    page_names_to_funcs = {
        "Train the BERT Model !!": train_page,
        "Test the BERT Model !!": test_page,
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()