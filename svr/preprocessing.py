import numpy as np
from scipy.signal import butter, filtfilt
import json

def readFileContent(file):
    """
    Reads file and return its contents
    """

    f = open(file)
    data = json.load(f)
    f.close()
    return data

def applyButterworthFilter(signal):
    # Sample rate
    fs = 100

    # Cutoff frequency
    cutoff_frequency = 3

    # Filter order
    filter_order = 3

    # Design a low-pass Butterworth filter
    b, a = butter(filter_order, cutoff_frequency / (fs / 2), btype='low', analog=False)

    output = filtfilt(b, a, signal)

    return output


def prepareDataSamples(data):
    """
    Prepares data samples
    """
    samples = []

    includeRawValues = False
    
    for d in data:
        if includeRawValues:
            x = np.array(list(zip(d['accelerationMagnitudeLeft'],d['accelerationMagnitudeRight'],
                    d['rawAccelerationXLeft'],d['rawAccelerationYLeft'],
                    d['rawAccelerationZLeft'],d['rawAccelerationXRight'],
                    d['rawAccelerationYRight'],d['rawAccelerationZRight'])))
            samples.append(x)
        else:
            # For left sensors
            leftX = applyButterworthFilter(d['rawAccelerationXLeft'])
            leftY = applyButterworthFilter(d['rawAccelerationYLeft'])
            leftZ = applyButterworthFilter(d['rawAccelerationZLeft'])

            # For right sensors
            rightX = applyButterworthFilter(d['rawAccelerationXRight'])
            rightY = applyButterworthFilter(d['rawAccelerationYRight'])
            rightZ = applyButterworthFilter(d['rawAccelerationZRight'])

            x = np.array(list(zip(leftX,leftY,leftZ,d['accelerationMagnitudeLeft'],rightX ,rightY,rightZ,d['accelerationMagnitudeRight'])))
            samples.append(x)

    return samples

def min_max_scaling(array_of_arrays,scaler):
    scaled_arrays = []

    for arr in array_of_arrays:
        original_shape = arr.shape
        arr = arr.reshape(1,-1)
        scaledData = scaler.transform(arr)
        scaledData = scaledData.reshape(original_shape)
        scaled_arrays.append(scaledData)

    return scaled_arrays