import sys
from collections import deque

sys.setrecursionlimit(10**6)

def adjacent_poper(N): #N을 입력받아 엣지리스트에서 N관계된건 다 없애버리고 인접버텍스는 리턴함
    #엣지리스트에서 N이 들어있는건 다 빼버려
    adjacents=[]
    for i in list(edge_list):
        if N in i:
            if i.index(N)==0:
                adjacents.append(i[1])
            elif i.index(N)==1:
                adjacents.append(i[0])
            edge_list.remove(i)
    #빼버리고 N 파트너는 리턴해버려
    return adjacents

def adjacent_poper2(N): #N을 입력받아 엣지리스트2에서 N관계된건 다 없애버리고 인접버텍스는 리턴함
    #엣지리스트2에서 N이 들어있는건 다 빼버려
    adjacents=[]
    for i in list(edge_list2):
        if N in i:
            if i.index(N)==0:
                adjacents.append(i[1])
            elif i.index(N)==1:
                adjacents.append(i[0])
            edge_list2.remove(i)
    #빼버리고 N 파트너는 리턴해버려
    return adjacents

edge_list=[]

input_string=sys.stdin.readline() #정점 수, 간선 수, 탐색시작점 입력받음
V,E,start=[int(i) for i in input_string.split()]

vertex_list=list(range(1,V+1))
vertex_list2=list(range(1,V+1))

for i in range(1,E+1):  #간선정보 반복문으로 입력받음
    edge=sys.stdin.readline()
    edge=[int(edge.split()[0]),int(edge.split()[1])]
    edge_list.append(edge)

edge_list2=list(edge_list)

DFS=''
stack=[]
stack.append(start)

BFS=''
deq=deque()
deq.append(start)
# for i in stack:
#     DFS=DFS+" "+str(stack.pop())
#     adjacents=adjacent_poper(i)
#     adjacents.sort(reverse=True)
#     for j in adjacents:
#         stack.append(j)

def DFS_runner(stack): #stack을 받아 dfs를 업데이트하고 업데이트된 stack을 return함. 재귀적으로 스택 없을때까지 반복
    global DFS
    global vertex_list
    temp=stack.pop()
    DFS=DFS+" "+str(temp)
    adjacents=list(set(adjacent_poper(temp)))
    for i in list(adjacents):   #파트너들중에 이미 큐에 잇는 중복된거는 제거하는 코드
        if i in list(stack):
            stack.remove(i)
    # print(adjacents)
    adjacents.sort(reverse=True)
    for j in adjacents:
        stack.append(j)
    if stack==[]:
        return
    if vertex_list==[]:
        return 
    elif stack!=[]:
        # print(vertex_list,stack,temp)
        vertex_list.remove(temp)
        # DFS=DFS+" "+str(temp)
        DFS_runner(list(stack))

def BFS_runner(deq): #que를 받아 bfs를 업데이트하고 업데이트된 que을 return함. 재귀적으로 큐 없을때까지 반복
    global BFS
    global vertex_list2
    temp=deq.popleft()     #큐에서 아래 뽑고
    BFS=BFS+" "+str(temp)
    adjacents=adjacent_poper2(temp) #뽑은거 파트너들 갖고오고
    for i in list(adjacents):   #파트너들중에 이미 큐에 잇는 중복된거는 제거하는 코드
        if i in list(deq):
            adjacents.remove(i)
    # DFS=DFS+" "+str(temp)
    adjacents.sort(reverse=False)   #정렬해서
    for j in adjacents:
        if j not in list(deq):
            deq.append(j)   #큐에넣음
    if list(deq)==[]:
        return
    # if vertex_list2==[]:    #버텍스 다 뽑았으면 끝 (빈틈있음)
    #     return 
    elif list(deq)!=[]:     #큐가 비지 않았으면
        # print(vertex_list2,deq,temp)
        if temp in vertex_list2:
            vertex_list2.remove(temp)
            # BFS=BFS+" "+str(temp)
        BFS_runner(deque(deq))

DFS_runner(stack)
print(DFS[1:])
BFS_runner(deq)
print(BFS[1:])