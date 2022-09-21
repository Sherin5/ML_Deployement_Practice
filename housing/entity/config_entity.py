from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", 
["dataset_download_url", "tgz_download_dir","raw_data_dir", "ingested_train_dir", "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", 
["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", 
["add_bedrron_per_room", "transformed_train_dir","transformed_test_dir", "preprocessed_object_file_path"])

model_trained_config = namedtuple("model_trained_config", ["trained_model_file_path", "base_accuracy"])

model_evaluation_config = namedtuple("model_evaluation_config", ["model_evaluation_file_path", "time_stamp"])

model_pusher_config = namedtuple("model_pusher_config", ["export_dir_path"])

Training_Pipeline_config = namedtuple("Training_Pipeline_config", ["artifact_dir"])
