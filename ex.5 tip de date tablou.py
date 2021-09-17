
n=int(input("Dati numarul de caratere din primul sir="))
m=int(input("Dati numarul de caratere din al doilea sir="))
x=[]
y=[]
for i in range(n):
    b=int(input("x="))
    x.append(b)
for i in range(m):
    c=int(input("y="))
    y.append(c)
print ("Suma primelor trei componente ale lui x =",x[0]+x[1]+x[2])
print("Suma tuturor componentelor a lui y =",sum(y))
p=1
for i in range (len(x)):
    p=p*x[i]
print("produsul tutror terminilor a lui x=",p)
print("Valoare absolta a componentei a treia din y =",abs(y[2]))
print("Suma primelo componente din x si y=",x[0]+y[0])
