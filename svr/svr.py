import numpy as np
import pickle


# Load saved model
with open('svr.pkl','rb') as svrf:
    model = pickle.load(svrf)

# Load scaler
with open('svrScaler.pkl','rb') as svrScaler:
    scaler = pickle.load(svrScaler)

def compute_statistical_features(sequence):
    mean_values = np.mean(sequence, axis=0)
    std_deviation_values = np.std(sequence, axis=0)
    max_values = np.max(sequence, axis=0)
    min_values = np.min(sequence, axis=0)
    range_values = np.ptp(sequence, axis=0) 
    features = np.concatenate([mean_values, std_deviation_values, max_values, min_values, range_values])
    return features


def apply(features):
    preds = model.predict(features)
    # inverse transform preds
    preds = scaler.inverse_transform(preds)
    return preds


def predict(sequence):
    features = compute_statistical_features(sequence)
    preds = apply(features)
    return preds