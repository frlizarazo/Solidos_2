import sympy as sp
from sympy.abc import x

#%%defninmos parametros
#geometria y propiedades mecanicas
b     = 0.05                 #ancho de la viga      m
h     = 0.25                 #altura de la viga     m
E     = 20e6                 #modulo de elasticidad Pa
I     = (b*h**3)/12

#carga distribuida
qd   = 100*x/3 - 300      #funcion de la carga distribuida kN/m
xdi  = 3                  #inicio de la carga distribuida en metros
xdf  = 6                  #final  de la carga distribuida en metros

#momentos
m    = 80                  #magnitud del momento kN*m
xm   = 1                   #posicion del momento en metros

#%% definimos funciones auxiliares que usaremos mas adelante
integre =  lambda f, x : sp.integrate(f, x, meijerg=False) #facilita la notacion al integrar
rect    =  lambda a,b,x: sp.Piecewise((0,x<a),(0,x>b),(1,True))  #permite aplicar una funcion solo en un tramo
int_mom =  lambda a,x  : sp.DiracDelta(x-a)
qdist = lambda f,a,b : sp.Piecewise((f, (a < x) & (x < b)), (0, True))
# sp.DiracDelta

#definimos el vector de cargas
q_sin_momento =qdist(qd,xdi,xdf)
mom           =m*int_mom(xm, x)

#%%resolvemos la ecuacion diferencial por tramo
#tramo 1
q1=q_sin_momento*rect(0, 1, x) 
V1 = integre(q1, x)+c1_1
t=integre(V1, x)+c1_2