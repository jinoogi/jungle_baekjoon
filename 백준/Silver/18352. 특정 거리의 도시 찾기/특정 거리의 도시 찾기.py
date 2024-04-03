import sys
from collections import deque
N,M,K,X=map(int,sys.stdin.readline().split()) #초기정보 입력받음

# 인접리스트 뼈대 생성
adjacent_matrix=[]
for _ in range(0,N):
    adjacent_matrix.append([])

for _ in range(0,M):
    i,j=map(int,sys.stdin.readline().split())
    adjacent_matrix[i-1].append(j)

# print(adjacent_matrix)

deq=deque()

def BFS(num): #번호 입력하면 그점부터 BFS실시
    distance=[-1]*N
    distance[num-1]=0
    deq.append(num)

    while True:
        if len(deq)==0:
            break
        poped=deq.popleft()
        for i in adjacent_matrix[poped-1]:
            if distance[i-1]==-1:
                deq.append(i)
                distance[i-1]=distance[poped-1]+1
    return distance
    

distance=BFS(X)
# distance[X-1]=0

# print(distance)

for city,dist in enumerate(distance):
    if dist==K:
        print(city+1)

if K not in distance:
    print(-1)
