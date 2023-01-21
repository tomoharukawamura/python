import numpy as np
#行列Aを生成
def prepare_matrix(n):
  matrix=np.zeros((n,n))
  for i in range(n-1,-1,-1):
    if i==n-1:
      matrix[i][i]=-1
    else:
      matrix[i][i]=-2
      matrix[i][i+1]=1
      matrix[i+1][i]=1
      
  return matrix

