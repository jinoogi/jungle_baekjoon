import sys
V=int(sys.stdin.readline())# 도시의 개수 입력받음
E=int(sys.stdin.readline())# 버스의 개수 입력받음

edge_list=[]
for _ in range(0,V+1): #버스 정보담은 엣지리스트 초기화
    edge_list.append([])

for x in range(1,E+1):
    i,j,cost=map(int,sys.stdin.readline().split()) #간선정보 입력받음
    edge_list[i].append([j,cost])

A,B=map(int,sys.stdin.readline().split()) #출발,도착도시 정보 받음

cost_list=[] #도시들의 비용 초기화
end_stack=[]
visited_list=[] #도시 방문여부 초기화
for _ in range(0,V+1): #최소비용 리스트,방문여부 리스트 초기화. 인덱스 맞추려고 0도 포함
    cost_list.append(float('inf'))
    visited_list.append(False)

now=A #현재위치 now에 저장
cost_list[now]=0 #출발지 0으로 시작
end_stack.append(now)

while True:
    visited_list[now]=True
    end_stack.pop()
    # if False not in visited_list: #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 힙이 비면 break로 o(1)가능할듯
    #     break
    for x in edge_list[now]:    #edge_list[now]는 now에서 갈수있는 [점,비용] 리스트들 #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if visited_list[x[0]]==False:
            if cost_list[x[0]]==float('inf') and cost_list[now]+x[1]!=float('inf'):
                end_stack.append(x[0])
            cost_list[x[0]]=min(cost_list[x[0]],cost_list[now]+x[1])   #최소비용 비교후 업데이트 . x[0]는 점, x[1]은 비용

    if end_stack==[]:
        break

    not_visited_list=[]     #미방문중 최소비용도시 찾기위한 똥꼬쇼 시작------------------------
    for i,is_visited in enumerate(visited_list): #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if is_visited==False:
            not_visited_list.append(i)

    not_visited_cost_list=[] 
    for i in not_visited_list: #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        not_visited_cost_list.append(cost_list[i])
    # print(end_stack)
    # print(not_visited_cost_list)
    #이 최소비용을 갖고있는 미방문지가 어딘지 찾는코드
    min_val=min(not_visited_cost_list)
    for i in not_visited_list:
        if cost_list[i]==min_val:
            min_city=i
            break
    # print(min_city)
    # print("---------------------")




    # min_city=cost_list.index(min(not_visited_cost_list)) #똥꼬쇼 종료------------------------ #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    now=min_city

# print(cost_list)
print(cost_list[B])


# 4
# 3
# 1 3 0
# 3 2 0
# 2 4 0
# 1 4