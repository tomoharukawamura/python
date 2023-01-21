import numpy as np
from . import utils

def create_mesh(node_x):
    mesh=[]
    for i in range(len(node_x)):
        data=[]
        for j in range(len(node_x)):
            data.append({
                'x':node_x[j],
                'y':1 if i==j else 0
            })
        mesh.append(data)
    return mesh

def create_stiffness_matriv(func_data):
    n=len(func_data)
    res=np.zeros((n,n))
    for i in range(n-1):
        slope_1=(func_data[i][i+1]['y']-func_data[i][i]['y'])/(func_data[i][i+1]['x']-func_data[i][i]['x'])
        slope_2=(func_data[i+1][i+1]['y']-func_data[i+1][i]['y'])/(func_data[i+1][i+1]['x']-func_data[i+1][i]['x'])
        el_1=(slope_1**2)*(func_data[i][i+1]['x']-func_data[i][i]['x'])
        el_2=slope_1*slope_2*(func_data[i][i+1]['x']-func_data[i][i]['x'])
        el_3=(slope_2**2)*(func_data[i][i+1]['x']-func_data[i][i]['x'])
        res[i][i]+=el_1
        res[i][i+1]+=el_2
        res[i+1][i]+=el_2
        res[i+1][i+1]+=el_3
    return res

def create_unknown_term_matrix(A):
    A_1=np.copy(A)
    res=np.zeros((len(A_1)-2,len(A_1)-2))
    for i in range(len(A_1)-2):
        for j in range(len(A_1)-2):
            res[i][j]+=A_1[i+1][j+1]
    return res

def create_known_term_matrix(A):
    A_2=np.copy(A)
    res=np.zeros((len(A_2)-2,2))
    for i in range(len(A_2)-2):
        res[i][0]+=A_2[i+1][0]
        res[i][1]+=A_2[i+1][len(A_2)-1]
    return res

def calc_answer(node):
    n=len(node)-2
    border_condition=np.array([0,1])
    fs=np.zeros(n)

    mesh_data=create_mesh(node)
    internal_matrix=create_stiffness_matriv(mesh_data)
    known_term_matrix=create_known_term_matrix(internal_matrix)
    unknown_term_matrix=create_unknown_term_matrix(internal_matrix)

    internal_right_hand=fs-utils.matvec(known_term_matrix,border_condition)
    unknown_term_matrix_inv=utils.calc_inverse_matrix(n,unknown_term_matrix)
    res_internal=utils.matvec(unknown_term_matrix_inv,internal_right_hand)

    res=[border_condition[0],border_condition[1]]
    for i in range(len(res_internal)):
        res.insert(i+1,res_internal[i])
    
    return res

