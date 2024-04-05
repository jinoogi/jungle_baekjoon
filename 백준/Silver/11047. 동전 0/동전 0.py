import sys
N,K=map(int,sys.stdin.readline().split()) #N,K입력받음


coins=[]
for _ in range(0,N):
    coins.append(int(sys.stdin.readline()))

def largest_coin_finder(balance): #현재 잔액을 입력받아 줄 수 있는 가장 큰 동전 반환
    for coin in reversed(coins):
        if coin > balance:
            continue
        elif coin <= balance:
            return coin
        
coin_count=0

balance=K
while True:
    if balance==0:
        break
    
    n=balance//largest_coin_finder(balance)
    balance=balance-largest_coin_finder(balance)*n
    coin_count=coin_count+n



    # balance=balance-largest_coin_finder(balance)
    # coin_count=coin_count+1

print(coin_count)