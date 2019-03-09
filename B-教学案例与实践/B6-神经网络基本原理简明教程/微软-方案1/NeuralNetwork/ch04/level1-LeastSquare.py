# 用最小二乘法得到解析解LSE

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
        return X, Y
    else:
        return None,None

# 根据公式8
def method1(X,Y,m):
    x_mean = np.mean(X)
    p = sum(Y*(X-x_mean))
    q = sum(X*X) - sum(X)*sum(X)/m
    w = p/q
    return w

# 根据公式9
def method2(X,Y,m):
    x_mean = sum(X)/m
    y_mean = sum(Y)/m
    p = sum(X*(Y-y_mean))
    q = sum(X*X) - x_mean*sum(X)
    w = p/q
    return w

# 根据公式6
def method3(X,Y,m):
    m = X.shape[0]
    p = m*sum(X*Y) - sum(X)*sum(Y)
    q = m*sum(X*X) - sum(X)*sum(X)
    w = p/q
    return w

# 根据公式7
def calculate_b(X,Y,w,m):
    b = sum(Y-w*X)/m
    return b

if __name__ == '__main__':
    X,Y = ReadData()
    m = X.shape[0]
    w1 = method1(X,Y,m)
    b1 = calculate_b(X,Y,w1,m)

    w2 = method2(X,Y,m)
    b2 = calculate_b(X,Y,w2,m)

    w3 = method3(X,Y,m)
    b3 = calculate_b(X,Y,w3,m)

    print("w1=%f, b1=%f" % (w1,b1))
    print("w2=%f, b2=%f" % (w2,b2))
    print("w3=%f, b3=%f" % (w3,b3))

