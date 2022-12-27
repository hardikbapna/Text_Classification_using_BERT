#This class is used to load the trained model.

import tensorflow as tf
import os

class LoadModel():

    def __init__(self, path):
        self.path= path
        self.load_model()


    def load_model(self):
        try:
            print("Loading  the model")
            trained_path= self.path + '\Trained_Models\sentiment_model'
            loaded_model = tf.keras.models.load_model(trained_path)
            print("Loaded the model")

        except Exception as e:
            print("Entered Exception: Model could not be loaded.")
            print("Error is: {}".format(e))


print("Remove")