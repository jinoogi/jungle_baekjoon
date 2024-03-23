count=0
calculation_result={} #계산결과 재활용시키기 위한 딕셔너리

def f(i,n,S,G): #f((i~n층),가->다)=f((i~n층),S->G)
    B="123".replace(S,'')
    B=B.replace(G,'')

    if(i==n):
        print(S+" "+G)

    else:
        f(i+1,n,S,B)
        print(S+" "+G)
        f(i+1,n,B,G)

def g(i,n,S,G): #f((i~n층),가->다)=f((i~n층),S->G)
    global count

    B="123".replace(S,'')
    B=B.replace(G,'')

    if i in calculation_result:
        count=count+calculation_result[i]

    elif(i==n):
        count=count+1

    else:
        g(i+1,n,S,B)
        count=count+1
        g(i+1,n,B,G)

x=int(input()) #하노이탑 몇층 할건지 질문
if x<=20:
    g(1,x,"1","3")
    print(count)
    f(1,x,"1","3")

else:
    for j in range(x,0,-1):
        g(j,x,"1","3")
        calculation_result[j]=count
        count=0
        

    g(1,x,"1","3")
    # print(count)
    # print(calculation_result)
    print(calculation_result[1])