#%% Importar Librerias
from sympy import *

#%% Defninmos Parametros

# Definir Variables Simbolicas

[x, c1_1, c1_2, c1_3, c1_4, \
    c2_1, c2_2, c2_3, c2_4, \
    c3_1, c3_2, c3_3, c3_4, \
    c5_1, c5_2, c5_3, c5_4, \
    c4_1, c4_2, c4_3, c4_4] = symbols(['x', 'c1_1', 'c1_2', 'c1_3', 'c1_4', \
                                            'c2_1', 'c2_2', 'c2_3', 'c2_4', \
                                            'c3_1', 'c3_2', 'c3_3', 'c3_4', \
                                            'c5_1', 'c5_2', 'c5_3', 'c5_4', \
                                            'c4_1', 'c4_2', 'c4_3', 'c4_4'])

for i in range(1,4):
    globals()[f'c{i}_{i}']=Symbol(f'c{i}_{i}')

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

integre =  lambda f, x : integrate(f, x, meijerg=False) #facilita la notacion al integrar
rect    =  lambda a,b,x: Piecewise((0,x<a),(0,x>b),(1,True))  #permite aplicar una funcion solo en un tramo
int_mom =  lambda a,x  : DiracDelta(x-a)
qdist   = lambda f,a,b : Piecewise((f, (a < x) & (x < b)), (0, True))
# sp.DiracDelta

#definimos el vector de cargas
q_sin_momento =qdist(qd,xdi,xdf)
mom           =m*int_mom(xm, x)

#%%resolvemos la ecuacion diferencial por tramo
#tramo 1
q1=q_sin_momento*rect(0, 1, x) 
V1 = integre(q1, x)+c1_1
t=integre(V1, x)+c1_2