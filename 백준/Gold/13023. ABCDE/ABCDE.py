import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    global found
    if depth == 4:
        found = True
        return
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
            if found:  # 추가된 종료 조건
                return
    visited[v] = False

found = False
for i in range(N):
    dfs(i, 0)
    if found:
        print(1)
        break
else:
    print(0)
