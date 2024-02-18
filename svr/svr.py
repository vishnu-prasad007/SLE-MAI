import numpy as np
import pickle
import preprocessing as utils

# Load saved Support Vector Regression (SVR) model from file
with open('svr.pkl', 'rb') as svrf:
    model = pickle.load(svrf)

# Load scaler for input features (scalerX) from file
with open('svrScalerX.pkl', 'rb') as svrScalerX:
    scalerX = pickle.load(svrScalerX)

# Load scaler for target values (scalerY) from file
with open('svrScaler.pkl', 'rb') as svrScalerY:
    scalerY = pickle.load(svrScalerY)

# Function to compute statistical features from a sequence
def compute_statistical_features(sequence):
    # Compute mean, standard deviation, maximum, minimum, and range values for each feature in the sequence
    mean_values = np.mean(sequence, axis=0)
    std_deviation_values = np.std(sequence, axis=0)
    max_values = np.max(sequence, axis=0)
    min_values = np.min(sequence, axis=0)
    range_values = np.ptp(sequence, axis=0) 
    # Concatenate computed statistical features into a single feature vector
    features = np.concatenate([mean_values, std_deviation_values, max_values, min_values, range_values])
    return features

# Function to apply the SVR model to predict outcomes based on input features
def apply(features):
    # Predict outcomes using the loaded SVR model
    preds = model.predict(features)
    # Inverse transform predicted values to original scale using scalerY
    original_shape = preds.shape
    preds = np.array(preds).reshape(-1, 1)
    preds = scalerY.inverse_transform(preds)
    preds = preds.reshape(original_shape)
    return preds

# Function to predict outcomes based on input features
def predict(features):
    # Apply the SVR model to compute predictions
    preds = apply(features)
    return preds


def main():
    # Read data from file
    data = utils.readFileContent('data/test/person6.json')

    # Prepare data samples
    data = utils.prepareDataSamples(data)

    # Initialize an empty list to store samples
    samples = []

    # Iterate through each data point
    for d in data:
        # Compute statistical features for each data point
        features = compute_statistical_features(d)
        
        # Append computed features to the samples list
        samples.append(features)

    # Scale input features using min-max scaling with scalerX
    samples = utils.min_max_scaling(samples, scalerX)
    
    # Predict outcomes using the prepared samples
    preds = predict(samples)

main()