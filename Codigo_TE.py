from sympy import *
from sympy.abc import x

init_printing()

# Caso 5: carga distribuida variable 
qdist = lambda f,a,b : Piecewise((f, (a < x) & (x < b)), (0, True))

# Funcion rectangular: si x>a y x<b retorne 1 sino retorne 0   
rect = lambda a,b : Piecewise((1, (a < x) & (x < b)), (0, True))

# Se define una función que hace el código más corto y legible
integre = lambda f, x : integrate(f, x, meijerg=False)

#%% Geometria y propiedades mecanicas
b     = 0.05                #ancho de la viga      m
h     = 0.25                #altura de la viga     m
E     = 2e7                 #modulo de elasticidad kPa
I     = (b*h**3)/12
alpha = 5/6
A     = b*h
nu    = 0.3
G     = E/(2*(1+nu))

k1,k2,k3 = 1000, 1000, 500

q = qdist(100*x/3-300,3,6)

x=symbols('x')
for i in range(1,5+1):
    for j in range(1,4+1):
        globals()[f'c{i}_{j}']=Symbol(f'c{i}_{j}')

#%%resolvemos la ecuacion diferencial por tramo

#tramo 1
q1 = q*rect(0, 1) 
V1 = integre(q1, x) + c1_1
M1 = integre(V1, x) + c1_2
t1 = integre(M1/(E*I), x) + c1_3
v1 = integre(t1-V1/(alpha*G*A), x) + c1_4

#tramo 2

q2 = q*rect(1, 3) 
V2 = integre(q2, x) + c2_1
M2 = integre(V2, x) + c2_2
t2 = integre(M2/(E*I), x) + c2_3
v2 = integre(t2-V2/(alpha*G*A), x) + c2_4

#tramo 3

q3 = q*rect(3, 4) 
V3 = integre(q3, x) + c3_1
M3 = integre(V3, x) + c3_2
t3 = integre(M3/(E*I), x) + c3_3
v3 = integre(t3-V3/(alpha*G*A), x) + c3_4
#tramo 4

q4 = q*rect(4, 5) 
V4 = integre(q4, x) + c4_1
M4 = integre(V4, x) + c4_2
t4 = integre(M4/(E*I), x) + c4_3
v4 = integre(t4-V4/(alpha*G*A), x) + c4_4
#tramo 5

q5 = q*rect(5, 6) 
V5 = integre(q5, x) + c5_1
M5 = integre(V5, x) + c5_2
t5 = integre(M5/(E*I), x) + c5_3
v5 = integre(t5-V5/(alpha*G*A), x) + c5_4

sol = solve([ 
    Eq(v1.subs(x,0), 0),               # despl vert en apoyo en x=0 es 0  
    #Eq(t1.subs(x,0), 0),               # theta en apoyo en x=0 es 0      
    Eq(diff(v1,x).subs(x,0), 0),               # theta en apoyo en x=0 es 0      
     
    Eq(v1.subs(x,1), - 0.03),            # despl vert en apoyo en x=1 es 0 
    Eq(v2.subs(x,1), - 0.03),            # despl vert en apoyo en x=1 es 0 
    Eq(t1.subs(x,1), t2.subs(x,1)),    # continuidad en theta en x=1     
    Eq(M1.subs(x,1), M2.subs(x,1) + 80),    # continuidad en M     en x=1  
       
    Eq(v2.subs(x,3), 0),               # despl vert en apoyo en  x=3 es 0 
    Eq(v3.subs(x,3), 0),               # despl vert en apoyo en  x=3 es 0 
    Eq(t2.subs(x,3), t3.subs(x,3)),    # continuidad en theta en x=3      
    Eq(M2.subs(x,3), M3.subs(x,3)),    # continuidad en M     en x=3    
      
    Eq(v3.subs(x,4), v4.subs(x,4)),                    # continuidad de desplazamientos
    Eq(M3.subs(x,4), M4.subs(x,4)),                    # continuidad en M     en x=4   
    Eq(t3.subs(x,4), t4.subs(x,4)),                    # continuidad en theta en x=4     
    Eq(V4.subs(x,4), V3.subs(x,4) - k1*v3.subs(x,4)),    #cortante en cada tramo 
    
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

V    = (V1*rect(0,1) + V2*rect(1,3) + V3*rect(3,4) + V4*rect(4,5) + V5*rect(5,6)).subs(sol)
M    = (M1*rect(0,1) + M2*rect(1,3) + M3*rect(3,4) + M4*rect(4,5) + M5*rect(5,6)).subs(sol)
t    = (t1*rect(0,1) + t2*rect(1,3) + t3*rect(3,4) + t4*rect(4,5) + t5*rect(5,6)).subs(sol)
v    = (v1*rect(0,1) + v2*rect(1,3) + v3*rect(3,4) + v4*rect(4,5) + v5*rect(5,6)).subs(sol)
dvdx = diff(v, x)

# %% Se imprimen los resultados 
print("\n\nV(x)     = "); pprint(V)
print("\n\nM(x)     = "); pprint(M)
print("\n\nt(x)     = "); pprint(t)
print("\n\nv(x)     = "); pprint(v)
print("\n\ndv_dx(x) = "); pprint(v)

# %% Se grafican los resultados 
x_xmin_xmax = (x, 0+0.001, 6-0.001)
plot(V,    x_xmin_xmax, xlabel='x', ylabel=    'V(x)')
plot(M,    x_xmin_xmax, xlabel='x', ylabel=    'M(x)')
plot(t,    x_xmin_xmax, xlabel='x', ylabel=    't(x)')
plot(v,    x_xmin_xmax, xlabel='x', ylabel=    'v(x)')
plot(dvdx, x_xmin_xmax, xlabel='x', ylabel='dv_dx(x)')

print(f'M(x=0)  = {float(    -M1 .subs(sol).subs(x,0))}')
print(f'Fy(x=0) = {float(     V1 .subs(sol).subs(x,0))}')
print(f'Fy(x=1) = {float(( V2-V1).subs(sol).subs(x,1))}')
print(f'Fy(x=3) = {float(( V3-V2).subs(sol).subs(x,3))}')
print(f'Fy(x=4) = {float((-k1*v3).subs(sol).subs(x,4))}')
print(f'Fy(x=5) = {float(( V5-V4).subs(sol).subs(x,5))}')
print(f'Fy(x=6) = {float((-k2*v5).subs(sol).subs(x,6))}')
print(f'M(x=6)  = {float((-k3*t5).subs(sol).subs(x,6))}')

#%%