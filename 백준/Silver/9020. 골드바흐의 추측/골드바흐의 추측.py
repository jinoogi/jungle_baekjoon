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

def goldbach(n):
    n_half=int(n/2)
    for i in range(0,n_half):
        if( prime_chekcer(n_half-i) and prime_chekcer(n/2+i) ):
            return(n_half-i,n_half+i)
#asd

T=int(input())
for times in range(1,T+1):
    i=int(input())
    print(goldbach(i)[0],goldbach(i)[1])