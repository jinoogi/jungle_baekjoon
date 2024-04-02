import sys 

def find(N): #N의 루트를 재귀적으로 찾음
    if N==union_list[N]:
        return N
    return find(union_list[N])

def union(a,b):
    root_a=find(a)
    root_b=find(b)
    if root_a!=root_b:
        if root_a<root_b:
            union_list[root_b]=root_a
        elif root_a>root_b:
            union_list[root_a]=root_b

N,M=map(int,sys.stdin.readline().split())   #정점의 개수와 간선의 개수 입력받음

union_list=list(range(0,N+1)) #인덱스랑 값 맞출려고 0포함해서 초기화
# print(union_list)

for _ in range(1,M+1):
    i,j=map(int,sys.stdin.readline().split())   #=간선정보 입력받음
    union(i,j)

union_status_list=[]

for i in range(1,N+1):
    union_status_list.append(find(i))

# union_status_list.remove(0) #인덱스 일치용 0 제거
print(len(list(set(union_status_list))))