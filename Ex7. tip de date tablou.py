v=[]
for i in range(7):
    x=int(input("v="))
    v.append(x)
z=['luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
print("venit saptamanal=",sum(v))
print("Venit zilnic mediu=",sum(v)/7)
print("Cel mai mare profit zilnic,",z[v.index(max(v))],"=",max(v))
print("Cel mai mic profit zilnic,",z[v.index(min(v))],"=",min(v))
