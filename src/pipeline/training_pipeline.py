import os 
import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

if __name__=="__main__":
    
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transforamtion=DataTransformation()
    train_arr,test_arr,_=data_transforamtion.initiate_data_transformation(train_data,test_data)
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))