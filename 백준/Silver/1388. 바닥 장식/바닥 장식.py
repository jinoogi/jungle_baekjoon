import sys

#N,M 입력받음
N,M=map(int,sys.stdin.readline().split()) 

floor=[]
transposed_floor=[]

for _ in range(0,N+1):
    floor.append([0]*(M+1))

for _ in range(0,M+1):
    transposed_floor.append([0]*(N+1))



#마룻바닥의 구조 2차원배열로 입력받음

for i in range(1,N+1): #인덱스 맞추기위해 하나 더 길게
    for j,x in enumerate(" "+sys.stdin.readline().strip()): #이것도 인덱스 맞추기위해 하나 더 길게
        floor[i][j]=x
        transposed_floor[j][i]=x


# for i in 

def widthblock_checker():
    global floor

    count=0
    for row in floor:
        past=False
        for now in row:
            if now =="-":
                if past==True:
                    continue
                elif past==False:
                    count=count+1
                    past=True
            else:
                past=False
    return count

def heightblock_checker():
    global transposed_floor

    count=0
    for row in transposed_floor:
        past=False
        for now in row:
            if now =="|":
                if past==True:
                    continue
                elif past==False:
                    count=count+1
                    past=True
            else:
                past=False
    return count

# print(floor)
# print(transposed_floor)
# print(widthblock_checker())
# print(heightblock_checker())
print(widthblock_checker()+heightblock_checker())
