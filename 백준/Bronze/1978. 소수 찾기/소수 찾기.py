def prime_chekcer(n):
    isprime=True
    if(n==1):
        isprime=False
    for i in range(2,int(n**0.5)+1):
        if((n//i)>1 and n%i==0 ):
            isprime=False
        else:
            pass
    return isprime

N=input()
numlist=input()
numlist=numlist.split()
numlist=[int(num) for num in numlist]

primelist=[]

for i in numlist:
    if prime_chekcer(i):
        primelist.append(i)
print(len(primelist))