# Q4 -  만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse = True)


def min_value(coins):
    
    if min(coins) > 1:
        return 1
    
    check = 0
    
    for i in range(sum(coins)-1):
        check = i
        for coin in coins:
            if check >= coin:
                check -= coin
                if check == 0:
                    break
        if check != 0:
            print(i)
            break
        
                    
                                              

min_value(coins)