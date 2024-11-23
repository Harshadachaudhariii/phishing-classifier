from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from pathlib import Path

def run_data_ingestion():
    data_ingestion = DataIngestion()
    raw_data_dir = data_ingestion.initiate_data_ingestion()
    print(f"Data Ingestion Completed. Data stored in: {raw_data_dir}")
    return raw_data_dir

def run_data_validation(raw_data_dir):
    data_validation = DataValidation(raw_data_store_dir=raw_data_dir)
    valid_data_dir = data_validation.initiate_data_validation()
    print(f"Data Validation Completed. Valid data stored in: {valid_data_dir}")
    return valid_data_dir

def run_data_transformation(valid_data_dir):
    data_transformation = DataTransformation(valid_data_dir=valid_data_dir)
    x_train, y_train, x_test, y_test, preprocessor_path = data_transformation.initiate_data_transformation()
    print("Data Transformation Completed.")
    return x_train, y_train, x_test, y_test, preprocessor_path

def run_model_training(x_train, y_train, x_test, y_test, preprocessor_path):
    model_trainer = ModelTrainer()
    model_score = model_trainer.initiate_model_trainer(x_train, y_train, x_test, y_test, preprocessor_path)
    print(f"Model Training Completed. Model score: {model_score}")
    return model_score

if __name__ == "__main__":
    raw_data_dir = run_data_ingestion()
    valid_data_dir = run_data_validation(raw_data_dir)
    x_train, y_train, x_test, y_test, preprocessor_path = run_data_transformation(valid_data_dir)
    model_score = run_model_training(x_train, y_train, x_test, y_test, preprocessor_path)
    print(f"Pipeline executed successfully. Trained model score: {model_score}")
