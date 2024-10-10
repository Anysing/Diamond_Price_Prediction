from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

## Data transformation config

@dataclass
class datatransformationconfig:
    preprocessor_file_path = os.path.join('artifacts','preprocessor.pkl')

class datatransformation:
    def __init__(self):
        self.transformation_config = datatransformationconfig()

    def get_data_transformation_obj(self):
        try:
            logging.info('Data transformation started')
            categorical_data = ['cut', 'color', 'clarity']
            numerical_data = ['carat', 'depth', 'table', 'x', 'y', 'z']

            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories = ['I1', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF', 'FL']

            logging.info('Pipeline initiated')

            # Numerical pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            # Categorical pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('OrdinalEncoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )
            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_data),
                ('cat_pipeline',cat_pipeline,categorical_data)
            ])

            return preprocessor
            logging.info('Pipeline completed')

        except Exception as e:
            logging.info('Error in pipeline')
            raise CustomException(e,sys)
                
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data')
            logging.info(f'Train DataFrame head : \n{train_df.head().to_string()}')
            logging.info(f'Test DataFrame head : \n{test_df.head().to_string()}')

            logging.info('Obtaining Preprocessing object')
            preprocessor_obj = self.get_data_transformation_obj()

            target_column_name = 'price'
            drop_columns = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Apply the transformation

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.fit_transform(input_feature_test_df)

            logging.info('Applying preprocessing object on Train and Test dataset')

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path=self.transformation_config.preprocessor_file_path,
                obj = preprocessor_obj
            )

            logging.info('Preprocessing pickle is created and saved')

            return (
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
## Data transformation config class
