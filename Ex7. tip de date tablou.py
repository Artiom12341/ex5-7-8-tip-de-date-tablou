v=[32,34,33,34,33,34,52]
z=['luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
print(v)
print("venit saptamanal=",sum(v))
print("Venit zilnic mediu=",sum(v)/7)
print("Cel mai mare profit zilnic=",z[v.index(max(v))],"=",max(v))
print("Cel mai mic profit zilnic=",z[v.index(min(v))],"=",min(v))
