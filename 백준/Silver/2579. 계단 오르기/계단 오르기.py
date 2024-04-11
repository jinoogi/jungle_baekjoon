import sys

N=int(sys.stdin.readline())
stairs=[0]
for _ in range(0,N):
    stairs.append(int(sys.stdin.readline()))
    
dp=[] # 1계단 스택 0,1,2 별로 따로관리 
for i in range(0,3):
    dp.append([0]*(N+1))

def dp_stairs():
    for i in range(1,N+1):  #dp[1 연속 스택][움직일 위치]
        if i ==1:
            dp[0][1]=stairs[i]
            continue
        dp[0][i]= max(dp[0][i-2],dp[1][i-2],dp[2][i-2])+stairs[i]
        dp[1][i]= dp[0][i-1]+stairs[i]
        # dp[2][i]= dp[1][i-1]+stairs[i]

dp_stairs()
# print(dp)
print(max(dp[0][N],dp[1][N]))