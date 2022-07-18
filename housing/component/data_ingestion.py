import sys,os
from housing.exception import HousingException
from housing.logger import logging
import tarfile #for data extraction
from six.moves import urllib #for downloading the data
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

#import config for this component
from housing.entity.config_entity import DataIngestionConfig

#import the artifacts that will be the output after dataingestion
from housing.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    """Class for data ingestion
    """

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        """Method starts the data ingestion process

        Args:
            data_ingestion_config (DataIngestionConfig): the config values taken from the /config/config.yaml file

        Raises:
            HousingException: Custome exception raised
        """
        try:
            logging.info(f"{'='*20}Data Ingestion Log Started{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HousingException(e,sys)
    
    def download_housing_data(self)-> str:
        """Method downloads the file and places it in the specified folder for extraction.

        Raises:
            HousingException: custom exception

        Returns:
            str: path to the downloaded file
        """
        try:
            #url for downloading
            download_url = self.data_ingestion_config.dataset_download_url
            
            #folder path to store the downloaded tgz file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            #get file name of the downloaded file
            housing_file_name = os.path.basename(download_url)

            #complete file path to download the file to
            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)

            #delete the folder if it already exists
            if os.path.exists(tgz_file_path):
                os.remove(tgz_file_path)
            
            #make the folder if it does not exist
            os.makedirs(tgz_file_path, exist_ok=True)

            #Now download
            logging.info(f"Downloading file from: [{download_url}] into: [{tgz_file_path}]")
            urllib.request.urlretrieve(download_url,tgz_file_path) 
            logging.info(f"File has been successfully downloaded to:[{tgz_file_path}]")
            
            return tgz_file_path

        except Exception as e:
            raise HousingException(e, sys) from e

    def extact_tgz_file(self, tgz_file_path:str):
        """extracts the file and places the extracted data in specific location

        Args:
            tgz_file_path (str): path to the downloaded file that needs to be extracted

        Raises:
            HousingException: custom exception
        """
        try:
            #get location to save extracted data
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            #delete the folder if it already exists
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            
            #make the folder if it does not exist
            os.makedirs(raw_data_dir, exist_ok=True)

            #exract data
            logging.info(f'Extracting tgz file: [{tgz_file_path}] into: [{raw_data_dir}]')
            
            with tarfile.open(tgz_file_path) as file_obj:
                file_obj.extractall(raw_data_dir)
            
            logging.info("Extraction Completed")
            
        except Exception as e:
            raise HousingException(e, sys) from e

    def split_data_as_train_test(self):
        try:
            #location folder of extracted data
            raw_data_dir=self.data_ingestion_config.raw_data_dir

            #get file name from the folder(there is only 1 file in folder)
            file_name=os.listdir(raw_data_dir)[0]

            #get complete path of extracted data
            housing_file_path=os.path.join(raw_data_dir, file_name)

            #create data frame
            housing_data_frame = pd.read_csv(housing_file_path)

            #Create a stratified split between train and test dataset. This will ensure the distribution of data
            #between train and test is similar
            #create additional col in df(used only for splitting data into train and test. it will be dropped before test and train data is set)
            housing_data_frame['income_cat']=pd.cut(
                housing_data_frame['median_income'],
                bins=[0.0,1.5,3.0,4.5,6.0,np.inf],
                labelss=[1,2,3,4,5]
            )

            strat_train_set= None
            strat_test_set= None

            #create a split parameter
            split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            #split the data
            for train_index, test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]):
                strat_train_set=housing_data_frame.loc[train_index].drop(["income_cat"], axis=1)
                strat_test_set=housing_data_frame.loc[test_index].drop(['income_cat'], axis=1)

            #get file paths for train and test
            train_file_path=os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)
            test_file_path=os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            #CONT FROM HERE=====================================================================


        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        """This method is a top level method. This method begins the data ingestion process and outputs the artifacts of the data ingestion component. All the other functions in data ingestion will be called from this method.

        Raises:
            HousingException: custom exception

        Returns:
            DataIngestionArtifact: The output of data ingestion
        """

        try:
            #downloaded data path
            tgz_file_path = self.download_housing_data()

            #extract the data
            self.extact_tgz_file(tgz_file_path=tgz_file_path)

        except Exception as e:
            raise HousingException(e, sys) from e


