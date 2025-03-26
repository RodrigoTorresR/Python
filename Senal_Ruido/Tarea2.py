#-----------PROGRAMA 2-----------
#Este programa muestra funciones senos
import numpy as np
import matplotlib.pyplot as plt
import math
pi = math.pi
#+++++ Defininimos las funciones +++++
def g(t,A = 1,f = 1/(2*pi),o =0):
    return A*np.sin((2*pi*f)*t + o)#A*np.sin(w*t + o)
def r1(t,A = 1, f = 1/(2*pi), o=0):
    return (A/6)*np.sin(8*(2*pi*f)*t + o)
def r2(t,A  = 1, f = 1/(2*pi), o = 0):
    return (A/10)*np.sin(16*(2*pi*f)*t + o)


#Valores constantes calculados para modificar la grafica
Periodos = 1 #Numero de periodos a mostrar
Vfrec1 = 1
frec1 = (1/(2*pi))*Vfrec1
Vfrec2 = 1
frec2 = (1/(2*pi))*Vfrec2
Vfrec3 = 1 
frec3 = (1/(2*pi))*Vfrec3

#Definimos los rangos de valores para los ejes X y Y
xlist = np.arange(0, Periodos*(2*pi), 0.01) #se indican cuantos peridos debemos mostrar
y1list = g(xlist, 1, frec1) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) + r1(xlist, 1, frec2) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) + r2(xlist, 1, frec3) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) + r1(xlist, 1, frec2) + r2(xlist, 1, frec3) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) * r1(xlist, 1, frec2) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) * r2(xlist, 1, frec3) #funcion: 1*seno(1*t + 0)
#y1list = g(xlist, 1, frec1) + r1(xlist, 1, frec2) + pow(r2(xlist, 1, frec3),2) #funcion: 1*seno(1*t + 0)
#y1list = pow(g(xlist, 1, frec1),2) + pow(r1(xlist, 1, frec2),2) + pow(r2(xlist, 1, frec3),2) #funcion: 1*seno(1*t + 0)
y2list = r1(xlist, 1, frec2) #funcion: 1*seno(1*t + 0)
y3list = r2(xlist, 1, frec3) #funcion: 1*seno(1*t + 0)

plt.figure(num=0, dpi=140)
plt.plot(xlist, y1list, label = "g(x)")
#plt.plot(xlist, y2list, label = "r1(x)")
#plt.plot(xlist, y3list, label = "r2(x)")

plt.title("Funcion Seno")
plt.xlabel("Pi Radianes")
plt.ylabel("Valores de la Función")
plt.legend()

plt.show()


