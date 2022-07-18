from collections import namedtuple

# DataIngestionConfig holds a tuple for the configuration required for data ingestion.
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

# dataset_download_url --> url for downloading the data
# tgz_download_dir --> location for downloaded zip file
# raw_data_dir --> location for extracted data
# ingested_train_dir --> Train dataset path
# ingested_test_dir --> Test dataset path
# Namedtouple is used because we do not want to change the config values once set (hence not using dictonary)


# Configuration for DataValidationConfig
DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path", "report_file_path","report_page_file_path"])
#schema_file_path --> path to the schema file. This file contains the information about the number of columns and their datatypes in the data
#report_file_path -->
#report_page_file_path -->

# Configuration for DataTransformationConfig
DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])
#add_betroom_per_room --> adds additional column to dataset (this is specific to this dataset)
# transformed_train_dir --> path for the transformed train data
# transformed_test_dir --> path for the transformed test data
# preprocessed_object_file_path --> pickle file for all the feature engineering steps

#Configuration for ModelTrainer
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])
# trained_model_file_path=location of the model pickle file
# base_accuracy = threshold accuracy below which the model will be rejected

# ModelEvaluationConfig
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])
# model_evaluation_file_path --> path to a file that contains information about all the models in prod currently. This info will be used to compare the newly trained model. If the newly trained model does not produce better results than the model in prod, the model in prod is not removed
# time_Stamp --> time stamp of when new model was created/ compared with prod

# ModelPusherConfigg
ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])
#export_dir_path --> location where the trained model is stored

#TrainingPipelineConfig
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
#artifact_dir --> location where pipelines details are stored

##Now all the parameters need to be passed to the project an hence need to be read from somewhere. This can be read from a DB, JSON, CSV , yaml files etc.