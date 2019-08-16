a=(input())
b=len(a)
c=[]
d=[]
f=''
h=''
for i in range(0,int(b),2):
    c.append(a[i])
for j in range(1,int(b),2):    
    d.append(a[j]) 
for e in c:
    f+=e
for g in d:
    h+=g
print(f,' ',h)
