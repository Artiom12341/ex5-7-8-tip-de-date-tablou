x=[]
for i in range(24):
    b=int(input("x="))
    x.append(b)
z=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
y=[]
print("temperatura medie=",sum(x)/24)
print("temperatura maxima=",max(x),'\n',"temperatura minima=",min(x),)
y=x.copy()
if x.count(max(x))>1:
    for i in range(24):
        if x[i]==max(x):
            print("la ora",z[x.index(max(x))]+1,"Temperatura maxima=",max(x))
            #del(x[i])
        else:
            print("-")
            #del(x[i])
else:
    print("temperatura maxima=",max(x),"la ora",z[x.index(max(x))])
if y.count(min(y))>1:
    for i in range(24):
        if y[i]==min(y):
            print("la ora",z[y.index(min(y))]+1,"Temperatura minima=",min(y))
            #del(y[i])
        else:
            print("-")
            #del(y[i])
else:
    print("temperatura minima=",min(x),"la ora",z[y.index(min(y))])



