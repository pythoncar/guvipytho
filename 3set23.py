dig=int(input())
num=list(map(int,input().split()))
if dig==len(num):
    num.sort()
    print(num[0])
