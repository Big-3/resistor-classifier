from pathlib import Path

def get_model_path():
	return str(Path(__file__).resolve().parent) + '/model.pkl'
