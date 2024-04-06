import sys

a=" "+sys.stdin.readline().strip()
b=" "+sys.stdin.readline().strip()

LCS_matrix=[]

for _ in range(0,len(a)):
    LCS_matrix.append([0]*(len(b)))

# print(LCS_matrix)

for i,char_a in enumerate(a):
    if i==0:
        continue
    for j,char_b in enumerate(b):
        if j==0:
            continue
        if char_a!=char_b:
            LCS_matrix[i][j]=max(LCS_matrix[i-1][j],LCS_matrix[i][j-1])
        elif char_a==char_b:
            LCS_matrix[i][j]=LCS_matrix[i-1][j-1]+1

# print(LCS_matrix)

print(LCS_matrix[len(a)-1][len(b)-1])