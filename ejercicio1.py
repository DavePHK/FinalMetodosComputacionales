# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while', solamente puede usar 'slicing' (i.e. a[2:-2])
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])


h = 0.001

fxx = fx + h
d=(fxx-fx)/h
print(d)

fxxx= d+h

dd = (fxxx-d)/h

plt.figure()
plt.scatter(x,dd)
plt.title('Segunda derivada')
plt.savefig('segunda.png')