import math as mt

x=float(input('digite un la distancia a la que esta el planeta (años luz): '))
v=float(input('digite la velocidad como fraccion de c:'))

xs=x*9460730472580800   #[m]
vc=v*3e8                
t=xs/vc 
print('el tiempo desde la tierra es: ', t )

gm=mt.sqrt(1-(v**2))
tn=(t-(v*xs)/3e8)/gm
print('el tiempo para la nave: ',tn)

