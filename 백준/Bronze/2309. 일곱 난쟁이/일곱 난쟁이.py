dwarfs=[]
for i in range(1,9+1): #난쟁이들 키 입력받음
    dwarf=int(input()) 
    dwarfs.append(dwarf)

i_break=False

for i in range(0,9):
    for j in range(0,9):
        if i==j:
            continue
        elif i!=j:
            ans=[item for index,item in enumerate(dwarfs) if index not in [i,j]]
            if sum(ans)==100:
                i_break=True
                break
    if i_break==True:
        break

ans.sort()
for i in ans:
    print(i)