#Used in predicting the sentiment.
from data_preprocessing import DataPreprocess
import tensorflow as tf
from Config_Files import testing_pipeline_config as config
import numpy as np

class Prediction():

    def __init__(self):
        self.preprocess_obj = DataPreprocess()
        trained_model_path= config.locations['trained_model_path']
        self.loaded_model = tf.keras.models.load_model(trained_model_path)


    def prediction_values(self, input_text):

        tokenized_input_text= self.preprocess_obj.prepare_data(input_text)
        probability = self.loaded_model.predict(tokenized_input_text)
        output_index = np.argmax(probability[0])
        output_prob = max(probability[0])

        return output_index, output_prob

