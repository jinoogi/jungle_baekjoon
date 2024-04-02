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

N=int(input())
M=int(input())

union_list=list(range(0,N+1)) #인덱스랑 값 똑같이 맞출려고 0 포함해서 리스트 생성

for _ in range(1,M+1):
    i,j=map(int,sys.stdin.readline().split())   #간선정보 입력받음
    union(i,j)

union_status_list=[]

for i in range(1,N+1):
    union_status_list.append(find(i))

count=0

for i in union_status_list: #각 요소의 루트를 표시해놓은 리스트를 돌면서 1과 일치하는 요소의 개수를 셈
    if i==union_status_list[0]:
        count=count+1
# print(union_status_list)
print(count-1)