from numpy.matrixlib.defmatrix import matrix
import matplotlib.pyplot as plt
import math
from . import utils
from . import matrix

#n番目の固有値と固有ベクトルを求める
def n_th_eigen_value(n,A,y_0,err,pre_eigen_vectors):
  y=y_0
  diff=1
  times=0
  while abs(diff) > err:
    times+=1
    internal_y=utils.matvec(n,A,y)
    in_for_y=internal_y
    for eigen_vec in pre_eigen_vectors:
      inner_pro_base=utils.inner_product(n,eigen_vec,internal_y)
      in_for_y-=inner_pro_base*eigen_vec
    internal_y=in_for_y
    y=internal_y/utils.norm2(n,internal_y)
    inner_pro=utils.inner_product(n,utils.matvec(n,A,y),y)
    if times>=2:
      diff=inner_pro - pre_res
    pre_res=inner_pro

  return {
      'vec':y,
      'val':inner_pro
  }

# まえの操作をn回繰り返す
def calc_eigen(n,y_0,is_inv):
  eigen_vecs=[]
  res_dict=[]
  A= utils.calc_inverse_matrix(n,matrix.prepare_matrix(n)) if is_inv else matrix.prepare_matrix(n)
  err=10**-10
  for i in range(1,n+1):
    dict=n_th_eigen_value(n,A,y_0,err,eigen_vecs)
    freqency=math.sqrt(-1/dict['val']) if is_inv else math.sqrt(-dict['val'])
    vec=dict['vec']
    eigen_vecs.append(vec)
    res_dict.append({
        'freq':freqency,
        'vec':vec
    })
    
  return res_dict

# プロットする
def plot_and_freq(y,is_inv):
  dicts=calc_eigen(len(y),y,is_inv)
  for dict in dicts:
    vec=[0]
    for num in dict['vec']:
      ratio= num/dict['vec'][0]
      vec.append(ratio)
    plt.plot(vec)
    vec.pop(0)
    dict['vec']=vec
  print(dicts)
  plt.show()