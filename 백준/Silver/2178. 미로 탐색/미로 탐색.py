from collections import deque
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())

matrix=[]
for _ in range(1,N+1):
    row=[int(i) for i in input()]
    matrix.append(row)

deq=deque()
deq.append([0,0])
matrix[0][0]=1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def BFS(deq): #시작점 입력하면 BFS 실시
    if list(deq)==[]:
        return
    x,y=deq.popleft()
    for i in range(0,4): #상하좌우탐색
        next_x,next_y=x+dx[i],y+dy[i]
        # print(next_x,next_y)
        if 0<=next_x<M and 0<=next_y<N:
            if matrix[next_y][next_x]==1:
                matrix[next_y][next_x]=matrix[y][x]+1
                deq.append([next_x,next_y])
    BFS(deq)

# print(matrix)
BFS(deq)
# print(matrix)
print(matrix[N-1][M-1])