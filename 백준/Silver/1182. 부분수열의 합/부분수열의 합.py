from itertools import combinations

N_S_string=input() #수열 길이 N,목표 S 스페이스로 구분해서 입력받음
N,S=int(N_S_string.split()[0]),int(N_S_string.split()[1])
num_list=input() #수열 스페이스로 구분해서 입력받음
num_list=num_list.split()
num_list=[int(i) for i in num_list]

# print(list(combinations(num_list,2)))

count=0

for i in range(1,len(num_list)+1):
    for j in list(combinations(num_list,i)):
        if sum(j)==S:
            count=count+1

print(count)