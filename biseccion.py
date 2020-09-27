# Algoritmo de Bisección
# [a,b] se escogen de la gráfica de la función
# error = tolera
import numpy as np

# INGRESO


def fx(x): return x**3 + 4*x**2 - 10


a = 1
b = 2
tolera = 0.001

# PROCEDIMIENTO
tabla = []
tramo = b-a

fa = fx(a)
fb = fx(b)
i = 1
while (tramo > tolera):
    c = (a+b)/2
    fc = fx(c)
    tabla.append([i, a, c, b, fa, fc, fb, tramo])
    i = i+1

    cambia = np.sign(fa)*np.sign(fc)
    if (cambia < 0):
        b = c
        fb = fc
    else:
        a = c
        fa = fc
    tramo = b-a
c = (a+b)/2
fc = fx(c)
tabla.append([i, a, c, b, fa, fc, fb, tramo])
tabla = np.array(tabla)

raiz = c

# SALIDA
np.set_printoptions(precision=4)
print('[ i, a, c, b, f(a), f(c), f(b), tramo]')
# print(tabla)

# Tabla con formato
n = len(tabla)
for i in range(0, n, 1):
    unafila = tabla[i]
    formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
    unafila = formato.format(*unafila)
    print(unafila)

print('raiz: ', raiz)
