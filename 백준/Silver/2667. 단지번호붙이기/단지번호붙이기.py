import sys

N= int(sys.stdin.readline())

complex_matrix=[]
complex_matrix.append([]) #인덱스맞추기용
for i in range(0,N):
    row = [int(i) for i in "0"+sys.stdin.readline().strip()]
    complex_matrix.append(row)

union_matrix=[]
union_matrix.append([])
for i in range(0,N+1):
    union_matrix.append([" "]*(N+1))
for i in range(1,N+1):
    for j in range(0,N+1):
        if complex_matrix[i][j]==1:
            union_matrix[i][j]=[i,j]

# print(complex_matrix)
# print(union_matrix)

def find(X): #좌표 입력하면 루트 찾아줌
    i,j=X
    next_i,next_j=union_matrix[i][j]
    if i==next_i and j==next_j:
        return union_matrix[i][j]
    else:
        return(find(union_matrix[i][j]))

def union(A,B): # 좌표 두개 입력하면 큰놈으로 합쳐줌
    global union_matrix

    root_A=find(A)
    root_B=find(B)
    # print("------------------------")
    # print(A,B)
    # print(root_A,root_B)
    if root_A!=root_B:
        if root_A<root_B:
            union_matrix[root_B[0]][root_B[1]]=root_A
        elif root_A>root_B:
            union_matrix[root_A[0]][root_A[1]]=root_B

dx=[0,0,-1,1]
dy=[-1,1,0,0]

for i in range(1,N+1):
    for j in range(0,N+1):
        if complex_matrix[i][j]==1:
            for dir in range(0,4):
                next_y=i+dy[dir]
                next_x=j+dx[dir]
                if 0<=next_x<N+1 and 1<=next_y<N+1:
                    # print(next_x,next_y)
                    if complex_matrix[next_y][next_x]==1:
                        # print([i,j],[next_y,next_x])
                        # print(union_matrix[i][j],union_matrix[next_y][next_x])
                        union([i,j],[next_y,next_x])
                        
result=[]

for i in range(1,N+1):
    for j in range(0,N+1):
        if complex_matrix[i][j]==1:
            union_matrix[i][j]=find([i,j])
            result.append(find([i,j]))

result2=set([tuple(i) for i in result])

ans=len(result2)

# print(union_matrix)
print(ans)
result3=[]
for i in result2:
    result3.append(result.count(list(i)))

result3.sort()
for i in result3:
    print(i)