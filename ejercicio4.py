# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.5, y=-1.0, z=1.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sigma = 10
beta = 2.67
rho=28.0

t=0
x=0.5
y=-1.0
z=1.0
T=5.0









plt.figure()
plt.scatter(y,x)
plt.title('x vs y')
plt.xlabel('y')
plt.ylabel('x')
plt.savefig('xy.png')

plt.figure()
plt.scatter(z,x)
plt.title('x vs z')
plt.xlabel('z')
plt.ylabel('x')
plt.savefig('xz.png')
