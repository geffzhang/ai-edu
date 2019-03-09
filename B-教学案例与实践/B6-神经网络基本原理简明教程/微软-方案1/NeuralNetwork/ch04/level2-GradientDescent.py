# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

# 用单次迭代方式
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

x_data_name = "TemperatureControlXData.dat"
y_data_name = "TemperatureControlYData.dat"

def ReadData():
    Xfile = Path(x_data_name)
    Yfile = Path(y_data_name)
    if Xfile.exists() & Yfile.exists():
        X = np.load(Xfile)
        Y = np.load(Yfile)
        return X,Y
    else:
        return None,None

if __name__ == '__main__':
    eta = 0.1
    X, Y = ReadData()
    w, b = 0.0, 0.0
    #w,b = np.random.random(),np.random.random()
    # count of samples
    num_example = X.shape[0]
    for i in range(num_example):
        # get x and y value for one sample
        x = X[i]
        y = Y[i]
        # get z from x,y
        z = w*x+b
        # calculate gradient of w and b
        dz = z - y
        db = dz
        dw = dz * x
        # update w,b
        w = w - eta * dw
        b = b - eta * db

    print(w,b)