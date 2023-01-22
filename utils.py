import math
import numpy as np

# ベクトルxのL2ノルムを計算
def norm2(n, x):
    res = 0
    for i in range(n):
        res += x[i]**2
    res = math.sqrt(res)
    return res

# 行列Aとベクトルxの行列ベクトル積Axを計算
def matvec(n, A, x):
    res = np.zeros(n)
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += A[i][j]*x[j]
        res[i] = tmp

    return res

# ベクトルxとベクトルyの内積を計算
def inner_product(n, x, y):
    res = 0
    for i in range(n):
        res += x[i]*y[i]

    return res
