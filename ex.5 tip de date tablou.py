
x=[2,3,4,56,6,7,8]
y=[2,3,4,5,6,7,8]
print(x)
print(y)
c=x[0]+x[1]+x[2]
print ("Suma primelor trei componente ale lui x =",c)
print("Suma tuturor componentelor a lui y =",sum(y))
p=1
for i in range (len(x)):
    p=p*x[i]
print("produsul tutror terminilor a lui x=",p)
print("Valoare absolta a componentei a treia din y =",abs(y[2]))
print("Suma primelo componente din x si y=",x[0]+y[0])
