import numpy as np

from vector import angulo, alineados

x=np.array([1,0,0])

y=np.array([0,1,0])

m=np.array([-1,0,0])

print("="*60)
print("ÁLGEBRA VECTORIAL")
print("="*60)

print("x-y =",angulo(x,y))
print("x-(-x) =",angulo(x,m))
print("alineados x/m =",alineados(x,m))
