# Importing required libraries
import mlflow

# Starting the MLflow run
mlflow.start_run()
mlflow.log_metric("alpha", 123)
mlflow.end_run()
