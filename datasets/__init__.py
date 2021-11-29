from pathlib import Path

def get_train_dataset_directory():
	return str(Path(__file__).resolve().parent) + '/train'

def get_validation_dataset_directory():
	return str(Path(__file__).resolve().parent) + '/validation'	