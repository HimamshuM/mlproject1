## END to END ml Project

Steps :

1- Set the github repository 
a) new env
b) setup.py
c) requirements.txt

2- src folder and build the package. 

3- Create components folder --> insert modules which we gonna use. (data_ingestion, data_transformation,model_evaluation,model_trainer)

4- Create pipeline folder --> for pipeline creation. (train pipeline, prediction pipeline)

5- Create belpw files :
    a) exception.py
    b) logging.py
    c) utils.py

6- Component/data_ingestion : 

    Steps : 
            1. import below files 

                import os 
                import sys
                from src.exception import CustomException
                from src.logger import logging
                import pandas as pd
                from sklearn.model_selection import train_test_split
                from dataclasses import dataclass

            2. create config class where path for raw,train,test data is present. 
                
                @dataclass
                class DataIngestionConfig:

            3. Create data ingestion class

                a. create initiate (init) function  and store path from above class with an object -> ingestion_config
                b. create initiate_data_ingestion function and use try-except block.
                    A. read csv file using pandas 
                    B. make directory where we want to store data
                    C. save the raw data inthat directory using to_csv 
                    D. split the data
                    E. Store test and train data in that directory using to_csv
                    F. Return test and train data path


7. components/data_transformation 
    
    steps : 

        1. Import the below files. 

                import sys
                from src.logger import logging
                from src.exception import CustomException
                from dataclasses import dataclass
                import os. 

                    ----- below packages depends on requirement ----------
                import pandas as pd
                import numpy as np 
                from sklearn.compose import ColumnTransformer
                from sklearn.impute import SimpleImputer
                from sklearn.pipeline import Pipeline
                from sklearn.preprocessing import  StandardScaler,OneHotEncoder
        
        2. 