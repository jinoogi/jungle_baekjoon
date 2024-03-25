import sys
from collections import deque

que=deque()
sys.stdin.readline
N=int(sys.stdin.readline()) #몇번할껀지 입력받기
for i in range(1,N+1):
    command=sys.stdin.readline() #명령 입력받기
    command=command.split()
    if command[0]=="push":
        que.append(command[1])
    elif command[0]=="pop":
        if len(que)==0:
            print(-1)
        elif len(que)>=1:
            print(que[0])
            del que[0]
    elif command[0]=="size":
        print(len(que))
    elif command[0]=="empty":
        if len(que)==0:
            print(1)
        elif len(que)>=1:
            print(0)
    elif command[0]=="front":
        if len(que)==0:
            print(-1)
        elif len(que)>=1:
            print(que[0])
    elif command[0]=="back":
        if len(que)==0:
            print(-1)
        elif len(que)>=1:
            print(que[-1])