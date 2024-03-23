numlist=[]
N=int(input()) #몇번할껀지 입력받음
for i in range(1,N+1):
    elelment=int(input())
    numlist.append(elelment)
numlist.sort()
for i in numlist:
    print(i)