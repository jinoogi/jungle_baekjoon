import sys

sys.setrecursionlimit(10**7)
def cases(n): #칸 길이 n을 받아 몇개의 경우가 가능한지 재귀적으로 알려줌
    # D=[0]*(n+1)
    # D[1]=1
    # D[2]=2

    # if n >2:
    #     for i in range(3,n+1):
    #         D[i]=D[i-1]+D[i-2]
    D=[0,0]
    D[0]=1
    D[1]=2
    if n==1:
        return 1
    if n==2:
        return 2
    if n >2:
        for i in range(3,n+1):
            temp=D[1]%15746
            D[1]=D[0]%15746+D[1]%15746
            D[0]=temp
        return D[1]%15746

n=int(sys.stdin.readline())

print(cases(n)%15746)
