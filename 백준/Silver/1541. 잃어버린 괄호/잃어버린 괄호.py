import sys,re

string=sys.stdin.readline()

front_sum,rear_sum=0,0

if '-' in string:
    first_minus_idx=string.find('-')
    front=[int(num) for num in string[:first_minus_idx].split('+')]
    front_sum=sum(front)
    rear=[int(num) for num in re.split(r'[+-]', string[first_minus_idx+1:])]
    rear_sum=sum(rear)
else:
    front=[int(num) for num in string.split('+')]
    front_sum=sum(front)

print(front_sum-rear_sum)