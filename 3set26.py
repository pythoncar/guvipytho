dig=int(input())
number=list(map(int,input().split()))
if dig==len(number):
    n=list(sorted(number))
    
    print(*n)
    
