import os
import joblib
import numpy as np
from django.conf import settings

def predict_with_knn(data):
    model_path = os.path.join(settings.BASE_DIR, 'espressoapp', 'knn_model.pkl')
    scaler_path = os.path.join(settings.BASE_DIR, 'espressoapp', 'scalers.pkl')
    
    model = joblib.load(model_path)
    scalers = joblib.load(scaler_path)
    
    # Print scaler keys for debugging
    print(f"Scaler keys: {scalers.keys()}")
    
    scaled_data = []
    feature_mapping = {
        'gender': 'Choose your gender',
        'age': 'Age',
        'marital_status': 'Marital status',
        'anxiety': 'Do you have Anxiety?',
        'panic_attack': 'Do you have Panic attack?',
        'specialist_treatment': 'Did you seek any specialist for a treatment?',
        'year_of_study': 'Your current year of Study'
    }
    
    for feature, mapped_feature in feature_mapping.items():
        if mapped_feature not in scalers:
            raise KeyError(f"Feature '{mapped_feature}' not found in scalers")
        scaled_feature = scalers[mapped_feature].transform(np.array(data[feature]).reshape(1, -1))
        scaled_data.append(scaled_feature[0])
    
    scaled_data = np.array(scaled_data).reshape(1, -1)
    prediction = model.predict(scaled_data)[0]  # Ensure the prediction is an integer
    return 1 if prediction == 'Yes' else 0

def predict_with_decision_tree(data):
    model_path = os.path.join(settings.BASE_DIR, 'espressoapp', 'decision_tree_model.pkl')
    scaler_path = os.path.join(settings.BASE_DIR, 'espressoapp', 'scalers.pkl')
    
    model = joblib.load(model_path)
    scalers = joblib.load(scaler_path)
    
    # Print scaler keys for debugging
    print(f"Scaler keys: {scalers.keys()}")
    
    scaled_data = []
    feature_mapping = {
        'gender': 'Choose your gender',
        'age': 'Age',
        'marital_status': 'Marital status',
        'anxiety': 'Do you have Anxiety?',
        'panic_attack': 'Do you have Panic attack?',
        'specialist_treatment': 'Did you seek any specialist for a treatment?',
        'year_of_study': 'Your current year of Study'
    }
    
    for feature, mapped_feature in feature_mapping.items():
        if mapped_feature not in scalers:
            raise KeyError(f"Feature '{mapped_feature}' not found in scalers")
        scaled_feature = scalers[mapped_feature].transform(np.array(data[feature]).reshape(1, -1))
        scaled_data.append(scaled_feature[0])
    
    scaled_data = np.array(scaled_data).reshape(1, -1)
    prediction = model.predict(scaled_data)[0]  # Ensure the prediction is an integer
    return 1 if prediction == 'Yes' else 0
