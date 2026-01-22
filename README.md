# Water Quality Monitoring & ML Lifecycle Management
This repository contains an end-to-end Machine Learning pipeline for predicting water potability. It integrates MLflow for experiment tracking and model versioning, alongside a robust re-training strategy to mitigate data drift and ensure long-term model reliability.

## Project Overview
The goal of this project is to automate the classification of water samples as "Potable" or "Not Potable" based on chemical properties. Unlike a static model, this project implements a Model Maintenance Lifecycle where the model is stored, versioned, and updated as new environmental data becomes available.

### Key Features
The Automated Pipeline
This project implements a fully automated "Closed-Loop" ML system. Every stage, from raw data to a production-ready model, is orchestrated to minimize manual intervention.
### 1. Automated Data EngineeringDynamic Ingestion: 
The pipeline automatically fetches the latest water quality sensor data from cloud storage or local databases.Validation & Cleaning: Implements automated data validation checks (checking for missing values or out-of-range pH levels) before transformation.
Feature Pipeline: Automated scaling and imputation (using Scikit-learn Pipelines) ensure that preprocessing is identical during both training and real-time inference, preventing Training-Serving Skew.
### 2. Automated Training & Experiment TrackingHyperparameter Optimization:
Uses tools like Optuna or Scikit-learn’s GridSearchCV to automatically find the best parameters.MLflow Integration: Every training run is automatically logged.Parameters: Learning rate, max depth, $n$-estimators.Metrics: $R^2$, Accuracy, and $F_1$-score.Artifacts: Automated generation of Confusion Matrices and Feature Importance plots.
### 3. Automated Model Registry & DeploymentVersion Control:
New models are automatically registered in the MLflow Model Registry with unique version IDs.Stage Promotion: Logic-based promotion (e.g., if a model passes a 90% accuracy threshold, it is automatically moved to the "Staging" stage).
### 4. Automated Maintenance & Re-training LoopThis is the core of the project’s sustainability:Performance Monitoring:
The system continuously compares the current Production model's performance against new incoming ground-truth data.Drift Trigger: If the $F_1$-score drops below a pre-defined threshold (e.g., 0.85), a Re-training Trigger is fired.Champion-Challenger Logic: The system trains a "Challenger" model on the new data batch. It only replaces the "Champion" (current Production model) if the Challenger shows statistically significant improvement.
## Technical Stack
Language: Python 3.9+
ML Frameworks: Scikit-learn / XGBoost
Tracking & Registry: MLflow
Data Handling: Pandas, NumPy
Environment Management: Conda / Pipenv

## Model Registry Workflow
We use the MLflow Model Registry to handle the deployment lifecycle:None -> Staging: New models are initially vetted here.
Staging -> Production: Once the maintenance script confirms the new model outperforms the current champion.
Production -> Archived: Replaced models are kept for audit trails but taken out of the active inference path.

## Maintenance & Re-training 
The logic followed :Fetches the current Production model metrics.Trains a new model on the latest data.Compares the $F_1$ Score of both.If $New_{F1} > Current_{F1} + \epsilon$, the new model is promoted.

Model Promotion: The best-performing model is moved to the "Production" alias in the Registry.

Monitoring & Re-training: The system checks for performance degradation and triggers the maintenance script.
