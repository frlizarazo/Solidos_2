#%% Importar Librerias
from sympy import *
init_printing()
#%% Defninmos Parametros

# Definir Variables Simbolicas

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

#constantes resortes

k1=1000                  #kN/m
k2=1000                  #kN/m
k3=500                   #kN*m/rad

#momentos
m    = 80                  #magnitud del momento kN*m
xm   = 1                   #posicion del momento en metros

#%% definimos funciones auxiliares que usaremos mas adelante

integre =  lambda f, x : integrate(f, x, meijerg=False) #facilita la notacion al integrar
rect    =  lambda a,b: Piecewise((0,x<a),(0,x>b),(1,True))  #permite aplicar una funcion solo en un tramo
int_mom =  lambda a,x  : DiracDelta(x-a)
qdist   = lambda f,a,b : Piecewise((f, (a < x) & (x < b)), (0, True))
# sp.DiracDelta

#definimos el vector de cargas
q_sin_momento =qdist(qd,xdi,xdf)
mom           =m*int_mom(xm, x)

#%%resolvemos la ecuacion diferencial por tramo

#tramo 1
<<<<<<< HEAD
q1 = q_sin_momento*rect(0, 1, x) 
V1 = integre(q1, x)+ mom  + c1_1
M1 = integre(V1, x)       + c1_2
t1 = integre(M1, x)       + c1_3
v1 = integre(t1, x)       + c1_4

#tramo 2

q2 = q_sin_momento*rect(1, 3, x) 
V2 = integre(q2, x)+ mom  + c2_1
M2 = integre(V2, x)       + c2_2
t2 = integre(M2, x)       + c2_3
v2 = integre(t2, x)       + c2_4

#tramo 3

q3 = q_sin_momento*rect(3, 4, x) 
V3 = integre(q3, x)+ mom  + c3_1
M3 = integre(V3, x)       + c3_2
t3 = integre(M3, x)       + c3_3
v3 = integre(t3, x)       + c3_4
#tramo 4

q4 = q_sin_momento*rect(4, 5, x) 
V4 = integre(q2, x)+ mom  + c4_1
M4 = integre(V2, x)       + c4_2
t4 = integre(M2, x)       + c4_3
v4 = integre(t2, x)       + c4_4
#tramo 5

q5 = q_sin_momento*rect(5, 6, x) 
V5 = integre(q2, x)+ mom  + c5_1
M5 = integre(V2, x)       + c5_2
t5 = integre(M2, x)       + c5_3
v5 = integre(t2, x)       + c5_4

# %%
=======
q1 = q_sin_momento*rect(0, 1) 
V1 = integre(q1, x)+ mom  +c1_1
M1 = integre(V1, x)       +c1_2
t1 = integre(M1, x)       +c1_3
v1 = integre(t1, x)       +c1_4

#tramo 2

q2 = q_sin_momento*rect(1, 3) 
V2 = integre(q2, x)+ mom  +c2_1
M2 = integre(V2, x)       +c2_2
t2 = integre(M2, x)       +c2_3
v2 = integre(t2, x)       +c2_4

#tramo 3

q3 = q_sin_momento*rect(3, 4) 
V3 = integre(q3, x)+ mom  +c3_1
M3 = integre(V3, x)       +c3_2
t3 = integre(M3, x)       +c3_3
v3 = integre(t3, x)       +c3_4
#tramo 4

q4 = q_sin_momento*rect(4, 5) 
V4 = integre(q2, x)+ mom  +c4_1
M4 = integre(V2, x)       +c4_2
t4 = integre(M2, x)       +c4_3
v4 = integre(t2, x)       +c4_4
#tramo 5

q5 = q_sin_momento*rect(5, 6) 
V5 = integre(q2, x)+ mom  +c5_1
M5 = integre(V2, x)       +c5_2
t5 = integre(M2, x)       +c5_3
v5 = integre(t2, x)       +c5_4

#%% hallamos valor de las constantes
sol = solve([ 
    Eq(v1.subs(x,0), 0),               # despl vert en apoyo en x=0 es 0  
    Eq(t1.subs(x,0), 0),               # theta en apoyo en x=0 es 0      
     
    Eq(v1.subs(x,1), 0.03),            # despl vert en apoyo en x=1 es 0 
    Eq(v2.subs(x,1), 0.03),            # despl vert en apoyo en x=1 es 0 
    Eq(t1.subs(x,1), t2.subs(x,1)),    # continuidad en theta en x=1     
    Eq(M1.subs(x,1), M2.subs(x,1)),    # continuidad en M     en x=1  
       
    Eq(v2.subs(x,3), 0),               # despl vert en apoyo en  x=3 es 0 
    Eq(v3.subs(x,3), 0),               # despl vert en apoyo en  x=3 es 0 
    Eq(t2.subs(x,3), t3.subs(x,3)),    # continuidad en theta en x=3      
    Eq(M2.subs(x,3), M3.subs(x,3)),    # continuidad en M     en x=3    
      
    Eq(v3.subs(x,4), v4.subs(x,4)),                    # continuidad de desplazamientos
    Eq(M3.subs(x,4), M4.subs(x,4)),                    # continuidad en M     en x=4   
    Eq(t3.subs(x,4), t4.subs(x,4)),                    # continuidad en theta en x=4     
    Eq(V3.subs(x,4), V4.subs(x,4)-k1*v4.subs(x,4)),    #cortante en cada tramo 
    
    Eq(v4.subs(x,5), 0),               # despl vert en apoyo en  x=5 es 0 
    Eq(v5.subs(x,5), 0),               # despl vert en apoyo en  x=5 es 0 
    Eq(t4.subs(x,5), t5.subs(x,5)),    # continuidad en theta en x=5     
    Eq(M4.subs(x,5), M5.subs(x,5)),    # continuidad en M     en x=5  
    
    Eq(V5.subs(x,6), -k2*v5.subs(x,6)), #accion del resorte en la cortante
    Eq(M5.subs(x,6), -k3*t5.subs(x,6)), #accion del resorte en la cortante
    
],
[ 
     c1_1, c1_2, c1_3, c1_4, 
     c2_1, c2_2, c2_3, c2_4, 
     c3_1, c3_2, c3_3, c3_4, 
     c4_1, c4_2, c4_3, c4_4, 
     c5_1, c5_2, c5_3, c5_4 ])

#%%fusionamos formulas y reemplazamos constantes

V = (V1*rect(0,1) + V2*rect(1,3) + V3*rect(3,4) + V4*rect(4,5) + V5*rect(5,6)).subs(sol)
M = (M1*rect(0,1) + M2*rect(1,3) + M3*rect(3,4) + M4*rect(4,5) + M5*rect(5,6)).subs(sol)
t = (t1*rect(0,1) + t2*rect(1,3) + t3*rect(3,4) + t4*rect(4,5) + t5*rect(5,6)).subs(sol)
v = (v1*rect(0,1) + v2*rect(1,3) + v3*rect(3,4) + v4*rect(4,5) + v5*rect(5,6)).subs(sol)

# %% Se simplifica lo calculado por sympy
V = nsimplify(V.rewrite(Piecewise))                   
M = (M.rewrite(Piecewise)) #.nsimplify()                 
t = (t.rewrite(Piecewise))               #piecewise_fold  
v = (v.rewrite(Piecewise))               #piecewise_fold  

# %% Se imprimen los resultados 
print("\n\nV(x) = "); pprint(V)
print("\n\nM(x) = "); pprint(M)
print("\n\nt(x) = "); pprint(t)
print("\n\nv(x) = "); pprint(v)

# %% Se grafican los resultados 
x_xmin_xmax = (x, 0+0.001, 6-0.001)
plot(V, x_xmin_xmax, xlabel='x', ylabel='V(x)')
plot(M, x_xmin_xmax, xlabel='x', ylabel='M(x)')
plot(t, x_xmin_xmax, xlabel='x', ylabel='t(x)')
plot(v, x_xmin_xmax, xlabel='x', ylabel='v(x)')
>>>>>>> a559b37c70e03daa58b0b44978847e6f56748cc8
