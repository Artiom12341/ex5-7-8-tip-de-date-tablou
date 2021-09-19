x=[]
for i in range(24):
    b=int(input("x="))
    x.append(b)
print("temperatura medie=",sum(x)/24)
print("temperatura maxima=",max(x),'\n',"temperatura minima=",min(x),)
z=[]
if x.count(max(x))>1:
    for i in range(24):
        if x[i]==max(x):
            z.append(i+1)
    for i in z:
        print("La ora",i,"temperatura maxima=",max(x))    
else:
    print("temperatura maxima=",max(x),"la ora",x.index(max(x))+1)
c=[]
if x.count(min(x))>1:
    for i in range(24):
        if x[i]==min(x):
            c.append(i+1)
    for i in c:
        print("La ora",i,"temperatura minima=",min(x))    
else:
    print("temperatura minima=",min(x),"la ora",x.index(min(x))+1)



