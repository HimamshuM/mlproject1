import os 
import sys
import pandas as pd 
import numpy as np 
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV,train_test_split
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_array,test_array):
        try:
            logging.info("Split training and test input data")

            # X_train,y_train,X_test,y_test = train_test_split(
            #     train_array[:,:-1],
            #     train_array[:,-1],
            #     test_array[:,:-1],
            #     test_array[:,-1]
            # )

            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]


            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(), 
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            logging.info("++++++++++++++++ Model Training initated ++++++++++++++++")

            model_report:dict = evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            ## to get the best model score from dictionary
            best_model_score = max(sorted(model_report.values()))

            ## get best model name from dictionary 
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info(f"Both model found on both training and testing data")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
                
            predicted = best_model.predict(X_test)

            r_score = r2_score(y_test,predicted)
            return r_score

        except Exception as e:
            raise CustomException(e,sys)