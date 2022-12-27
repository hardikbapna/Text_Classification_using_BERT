#This file runs the main/app of the testing pipeline.

from Load_model import LoadModel
from Config_Files import testing_pipeline_config as config
import os


if __name__ == '__main__':

    print('Running the main function' )

    path= config.locations['path']
    LoadModel(path)

    print("Model is Loaded in main.")