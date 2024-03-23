def factorial(n): #n을 입력받아 팩토리얼출력
    result=1
    for i in range(n,1,-1):
        result=result*i
    return result


n=int(input()) #팩토리얼할 숫자를 입력받음
print(factorial(n))