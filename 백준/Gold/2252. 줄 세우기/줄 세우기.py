import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split()) #정점, 간선개수 입력받기

adj_list=[]
indegree_list=[]
visit_list=[]

for _ in range(0,N+1): # adj_list초기화, 인덱스 보기편하기 맞추려고 1개 더 길게 선언
    adj_list.append([])
    indegree_list.append([])
    visit_list.append(False)

for _ in range(0,M): # 간선정보 입력받기
    i,j=map(int,sys.stdin.readline().split())
    adj_list[i].append(j)
    indegree_list[j].append(i)

for x in range(0,N+1):
    indegree_list[x]=len(indegree_list[x]) # 전치-인접리스트에서 그냥 진입차수 개수 리스트로 변환

result=''

deq=deque()

# for x in range(1,N+1): #노드들을 전부 확인하며 진입차수가 0인거 찾고, 0이면 큐에 집어넣음
#     if indegree_list[x]==0 and not visit_list[x]:
#         deq.append(x)
#         visit_list[x]=True
#         result=result+" "+str(x)
# poped=deq.popleft()     #하나 큐에서 뽑기

# candidates=[] #시간복잡도 해결용으로 N^2이 안나오게 진입차수 빼진애들 재활용하기로 했음

# for j in adj_list[poped]:   #큐에서 뽑은애가 연결된게 있으면, 연결된애들의 진입차수 1뺌
#     indegree_list[j]=indegree_list[j]-1
#     candidates.append[j]

candidates=list(range(1,N+1))

while True:
    for x in candidates: #노드들을 전부 확인하며 진입차수가 0인거 찾고, 0이면 큐에 집어넣음
        if indegree_list[x]==0 and not visit_list[x]:
            deq.append(x)
            visit_list[x]=True
            result=result+" "+str(x)

    candidates=[] #다음 재활용을 위해 초기화

    if not deq:
        break
    poped=deq.popleft()     #하나 큐에서 뽑기
    for j in adj_list[poped]:   #큐에서 뽑은애가 연결된게 있으면, 연결된애들의 진입차수 1뺌
        indegree_list[j]=indegree_list[j]-1
        candidates.append(j)

print(result[1:])