from collections import namedtuple


#create a data ingestion artifact. Defines the outputs from data ingestion
DataIngestionArtifact=namedtuple(DataIngestionArtifact,["train_file_path","test_file_path","is_ingested","message"])
