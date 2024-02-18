import numpy as np
from scipy.signal import butter, filtfilt
import json

def read_file_content(file):
    """
    Reads file and returns its contents.
    """
    # Open the file and load its contents using JSON
    f = open(file)
    data = json.load(f)
    f.close()
    return data

def apply_butterworth_filter(signal):
    """
    Applies a Butterworth filter to the input signal.
    """
    # Sample rate
    fs = 100

    # Cutoff frequency
    cutoff_frequency = 3

    # Filter order
    filter_order = 3

    # Design a low-pass Butterworth filter
    b, a = butter(filter_order, cutoff_frequency / (fs / 2), btype='low', analog=False)

    # Apply the filter to the signal
    output = filtfilt(b, a, signal)

    return output


def prepare_data_samples(data):
    """
    Prepares data samples by applying Butterworth filter to raw accelerometer data.
    """
    samples = []

    includeRawValues = False
    
    for d in data:
        if includeRawValues:
            # If raw values are to be included, construct feature array directly from raw data
            x = np.array(list(zip(d['accelerationMagnitudeLeft'], d['accelerationMagnitudeRight'],
                    d['rawAccelerationXLeft'], d['rawAccelerationYLeft'],
                    d['rawAccelerationZLeft'], d['rawAccelerationXRight'],
                    d['rawAccelerationYRight'], d['rawAccelerationZRight'])))
            samples.append(x)
        else:
            # Apply Butterworth filter to left and right accelerometer data
            leftX = apply_butterworth_filter(d['rawAccelerationXLeft'])
            leftY = apply_butterworth_filter(d['rawAccelerationYLeft'])
            leftZ = apply_butterworth_filter(d['rawAccelerationZLeft'])
            rightX = apply_butterworth_filter(d['rawAccelerationXRight'])
            rightY = apply_butterworth_filter(d['rawAccelerationYRight'])
            rightZ = apply_butterworth_filter(d['rawAccelerationZRight'])

            # Construct feature array from filtered accelerometer data
            x = np.array(list(zip(leftX, leftY, leftZ, d['accelerationMagnitudeLeft'],
                                   rightX, rightY, rightZ, d['accelerationMagnitudeRight'])))
            samples.append(x)

    return samples

def min_max_scaling(array_of_arrays, scaler):
    """
    Performs min-max scaling on the input array of arrays using the provided scaler.
    """
    scaled_arrays = []

    for arr in array_of_arrays:
        # Reshape the array to 1D
        original_shape = arr.shape
        arr = arr.reshape(1, -1)
        
        # Perform scaling
        scaled_data = scaler.transform(arr)
        
        # Reshape back to original shape
        scaled_data = scaled_data.reshape(original_shape)
        
        scaled_arrays.append(scaled_data)

    return scaled_arrays