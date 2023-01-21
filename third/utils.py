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

# 逆行列を計算
def calc_inverse_matrix(n,A):
  B=np.eye(n)
  for j in range(0,n,1):
    for i in range(j+1,n,1):
      coe = -A[i][j]/A[j][j]
      for k in range(n):
        A[i][k]+=coe*A[j][k]
        B[i][k]+=coe*B[j][k]

  for j_2 in range(n-1,0,-1):
    for i_2 in range(j_2-1,-1,-1):
      coe_2 = -A[i_2][j_2]/A[j_2][j_2]
      for k_2 in range(n):
        B[i_2][k_2]+=coe_2*B[j_2][k_2]

  for i_3 in range(n):
    for j_3 in range(n):
      B[i_3][j_3]=B[i_3][j_3]/A[i_3][i_3]
      
  return B
