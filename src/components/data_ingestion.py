import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer



@dataclass
class DataIngestionConfig:
    ## providing path for csv files
    test_data_path:str = os.path.join("artifacts",'test.csv')
    train_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts",'data.csv')

class DataIngestion:
    def __init__ (self):
        self.ingestion_config= DataIngestionConfig()  ## initiating class for paths 

    def initiate_data_ingestion(self):
        logging.info("+++++++++++ Entered the data Ingestion component +++++++++++++++")
        try:
            ## reading data frame
            df = pd.read_csv('Notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            ## creating directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            ## csv file saving at raw data path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            ## Spliting raw data to train and test. 
            logging.info("Train test split initiated")
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=23)

            ## Creating and saving csv for train dataset in path mentioned in ingestion_config object
            train_df.to_csv(self.ingestion_config.test_data_path,index= False,header=True)

            ## Creating and saving csv for test dataset in path mentioned in ingestion_config object 
            test_df.to_csv(self.ingestion_config.test_data_path,header=True,index=False)

            logging.info("+++++++++++++++++ Data Ingestion Completed +++++++++++++++")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data= obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    
    
