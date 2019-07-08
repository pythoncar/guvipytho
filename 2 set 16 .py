k,a=map(int,input().split())
for r in range(k+1,a):
    for t in range(2,r):
        if(r%t==0):
            break
    else:
        
        print(r,end=' ')
        
