dig=int(input())
num=list(map(int,input().split()))
if dig==len(num):
    n=list(sorted(num))
    
    print(*n)
    
