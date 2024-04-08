import sys
N=int(sys.stdin.readline())

matrixes=[]

for i in range(0,N+1):
    if i==0:
        matrixes.append([])
    else:
        r,c=map(int,sys.stdin.readline().split())
        matrixes.append([r,c])

dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,N+1):
        if i==j:
            dp[i].append(0)
        else:
            dp[i].append(-1)

def min_updater(x,y): #x,y를 입력받고 재귀호출을 통해 x~y까지중에 가장 작은 곱셈횟수 리스트에 갱신
    min=float('inf')
    for i in range(x,y):
        if dp[x][i]==-1:
            min_updater(x,i)
        if dp[i+1][y]==-1:
            min_updater(i+1,y)
        temp=dp[x][i]+dp[i+1][y]+(matrixes[x][0]*matrixes[i][1]*matrixes[y][1])
        if temp<min:
            min=temp
        pass
    dp[x][y]=min

min_updater(1,N)

print(dp[1][N])
