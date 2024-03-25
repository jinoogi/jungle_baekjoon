import sys
string=sys.stdin.readline()
N=int(string.split()[0])
K=int(string.split()[1])
josephus_list=list(range(1,N+1))
temp_index=0

ans=[]

location=-1
for i in range(1,N+1):
    list_length=len(josephus_list)
    if (location+1)+K>list_length:
        target=(location)+K-list_length
        while target>=list_length:
            target=target-list_length
        location=target-1
    else:
        target=(location)+K
        location=target-1
    # print(josephus_list[target], target, location)
    ans.append(josephus_list[target])
    del(josephus_list[target])

list_str = str(ans)
# 대괄호를 꺾쇠 괄호로 변경
modified_str = list_str.replace('[', '<').replace(']', '>')
print(modified_str)


    # if(temp_index+K-1)>len(josephus_list): #실제 삭제되는 인덱스
    #     pass
    # if list_length<K:
    #     pass