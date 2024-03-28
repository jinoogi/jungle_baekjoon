def single_digit_checker(num): #숫자를 입력받아 2자리수이상이면 그냥 return, 1자릿수이면 2자릿수로 변환해서 반환
    if len(num) <2:
        return "0"+num
    elif len(num) >=2:
        return num
    
def first_digit_selector(num): #숫자를 입력받아 1의자릿수를 반환
    if len(num) <2:
        return num
    elif len(num) >=2:
        return num[1]

count=0
N=input() #N을 입력받음
num=single_digit_checker(N)
while True:
    num=single_digit_checker(num)
    sum=str(int(num[0])+int(num[1]))
    num=num[1]+first_digit_selector(sum)
    count=count+1
    if int(N)==int(num):
        break
print(count)