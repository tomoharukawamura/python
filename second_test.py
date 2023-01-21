from second import mesh
from numpy.matrixlib.defmatrix import matrix
import matplotlib.pyplot as plt

nodes=[]
for i in range(11):
    nodes.append(i*0.1)
ans=mesh.calc_answer(nodes)
plt.plot(nodes,ans)
plt.show()