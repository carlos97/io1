import numpy as np
import matplotlib.pyplot as plt

#f = lambda x,y : np.sqrt(2*x*y)-x-y
f = lambda x,y : 2*x+y
d = np.linspace(-100,100,2000)
x,y = np.meshgrid(d,d)
im1 = plt.imshow(((f(x,y)<5)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 1") 
plt.show()


f = lambda x,y : y
im2 = plt.imshow(((f(x,y)<=5)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 2") 
plt.show()


f = lambda x,y : 2*(2*x-y)
g = lambda x,y : 2*(x+y)-4
im2 = plt.imshow(((g(x,y)<=f(x,y))).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 3") 
plt.show()


f = lambda x,y : 2*x-y
g = lambda x,y : 2*y-1
im2 = plt.imshow(((f(x,y)>3) & (g(x,y)>0) & (x>=y)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 4") 
plt.show()


f = lambda x,y : 2*x-3*y
g = lambda x,y : x
h = lambda x,y : y
im2 = plt.imshow(((f(x,y)<=60) & (g(x,y)>=0) & (h(x,y)>=0)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 5") 
plt.show()


f = lambda x,y : 2*x+y
g = lambda x,y : x+2*y
h = lambda x,y : x+y

im2 = plt.imshow(((f(x,y)<=180) & (g(x,y)<=160) & (h(x,y)<=100) & (x>=0) & (y>=0)).astype(int),
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys")
plt.title("ejercicio 1 - 6") 
plt.show()



