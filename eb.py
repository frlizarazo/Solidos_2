#%% Importar Librerias
from sympy import *

#%% Defninmos Parametros

# Definir Variables Simbolicas

#[x, c1_1, c1_2, c1_3, c1_4, \
 #   c2_1, c2_2, c2_3, c2_4, \
  #  c3_1, c3_2, c3_3, c3_4, \
   # c5_1, c5_2, c5_3, c5_4, \
    #c4_1, c4_2, c4_3, c4_4] = symbols(['x', 'c1_1', 'c1_2', 'c1_3', 'c1_4', \
     #                                       'c2_1', 'c2_2', 'c2_3', 'c2_4', \
      #                                     'c5_1', 'c5_2', 'c5_3', 'c5_4', \
       #                                     'c4_1', 'c4_2', 'c4_3', 'c4_4'])
x=symbols('x')
for i in range(1,5+1):
    for j in range(1,4+1):
     globals()[f'c{i}_{j}']=Symbol(f'c{i}_{j}')

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
q1 = q_sin_momento*rect(0, 1, x) 
V1 = integre(q1, x)+ mom  +c1_1
M1 = integre(V1, x)       +c1_2
t1 = integre(M1, x)       +c1_3
v1 = integre(t1, x)       +c1_4

#tramo 2

q2 = q_sin_momento*rect(1, 3, x) 
V2 = integre(q2, x)+ mom  +c2_1
M2 = integre(V2, x)       +c2_2
t2 = integre(M2, x)       +c2_3
v2 = integre(t2, x)       +c2_4

#tramo 3

q3 = q_sin_momento*rect(3, 4, x) 
V3 = integre(q3, x)+ mom  +c3_1
M3 = integre(V3, x)       +c3_2
t3 = integre(M3, x)       +c3_3
v3 = integre(t3, x)       +c3_4
#tramo 4

q4 = q_sin_momento*rect(4, 5, x) 
V4 = integre(q2, x)+ mom  +c4_1
M4 = integre(V2, x)       +c4_2
t4 = integre(M2, x)       +c4_3
v4 = integre(t2, x)       +c4_4
#tramo 5

q5 = q_sin_momento*rect(5, 6, x) 
V5 = integre(q2, x)+ mom  +c5_1
M5 = integre(V2, x)       +c5_2
t5 = integre(M2, x)       +c5_3
v5 = integre(t2, x)       +c5_4
