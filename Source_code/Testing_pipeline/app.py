#This file runs the main/app of the testing pipeline.

from Config_Files import testing_pipeline_config as config
from prediction import Prediction

from Source_code.Testing_pipeline.Load_model import load_model

import os
load_model()

if __name__ == '__main__':




    print('Running the main function' )
    try:
        path= config.locations['path']
        input_text = 'I loved the movie'
        pred_obj= Prediction()
        output_index, output_prob= pred_obj.prediction_values(input_text)
        print("Output Index is: ", output_index)
        print("Output Probability is: ", output_prob)


        print("Model is Loaded in main.")

    except Exception as e:
        print (e)