import sys
stack=[]
sys.stdin.readline
N=int(sys.stdin.readline()) #몇번할껀지 입력받기
for i in range(1,N+1):
    command=sys.stdin.readline() #명령 입력받기
    command=command.split()
    if command[0]=="push":
        stack.append(command[1])
    elif command[0]=="pop":
        if len(stack)==0:
            print(-1)
        elif len(stack)>=1:
            print(stack[-1])
            del stack[-1]
    elif command[0]=="size":
        print(len(stack))
    elif command[0]=="empty":
        if len(stack)==0:
            print(1)
        elif len(stack)>=1:
            print(0)
    elif command[0]=="top":
        if len(stack)==0:
            print(-1)
        elif len(stack)>=1:
            print(stack[-1])