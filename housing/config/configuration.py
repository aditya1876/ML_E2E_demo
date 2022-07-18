from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig,TrainingPipelineConfig

#import helper functions
from housing.util.util import read_yaml_file

#import constant values
from housing.constant import *   

#import exception
from housing.exception import HousingException
#import logging
from housing.logger import logging
import sys


class Configuration:
    """_summary_: This class takes configuraiton information from /config/config.yaml and passes to /housing/entity/config_entity.py
    """

    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) -> None:
        try:
            #read the config file contents
            self.config_info=read_yaml_file(config_file_path)

            #get the training pipeline config
            self.training_pipeline_config = self.get_training_pipeline_config()

            #get timestamp
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e, sys) from e  

    def get_training_pipeline_config(self):
        """This function creates a pipeline configuration for the pipeline to use. It takes the config information from the constant folder and creates a config. This way we only need to udpate the config values once in the constant folder. Also once a config is set it cannot be udpated.

        Raises:
            HousingException: Raises custom exception for this project.

        Returns:
            namedtuple: location of artifact dir as a named touple with key as training_pipeline_config
        """
        try:

            #get the section where pipeline info is stored in the config.yaml file
            training_pipeline_info = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            #get the full path to the artifact directory
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_info[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_info[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            #now create a config
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)

            logging.info(f"training pipeline config: {training_pipeline_config}")

            return training_pipeline_config

        except Exception as e:
            raise HousingException(e, sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """This function gets the config values from constant folder and creates a namedtouple config for dataingestion component

        Returns:
            DataIngestionConfig: namedtouple of config required for data ingestion component. We are looking for a folder structure like /Housing/artifact/data_ingestion/<datetimestamp>/files.
            Files will have following structure
            datetimestamp
                - raw_data
                - tgz_data
                - ingested_data
                    - ingested_train_data
                    - ingested_test_data  
        """
        try:
            #artifact_dir=self.training_pipeline_config.artifact_dir
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            data_ingestion_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                DATA_INGESTION_ARTIFICT_DIR,
                self.time_stamp)
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            dataset_download_url=data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir=os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            ingested_train_dir=os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY],
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir=os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY],
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                raw_data_dir=raw_data_dir,
                tgz_download_dir=tgz_download_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir
                
            )

            logging.info(f'Data Ingestion Info: {data_ingestion_config}')

            return data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
        """This function gets the config information from the constant folder and creates a namedtuple for data validation component    

        Returns:
            DataValidationConfig: namedtuple that stores the config values for data validation component
        """
        try:
            #create the folder structure for data validation artifacts
            data_validaion_atrifact_dir=os.path.join(
                self.training_pipeline_config.artifact_dir, #housing/artifact
                DATA_VALIDATION_SCHEMA_DIR_KEY, #config
                self.time_stamp #timestamp
            )
            # /housing/artifact/config/timestamp

            
            data_validation_info=self.config_info[DATA_VALIDATION_CONGIF_KEY]

            

        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(slef) -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass
