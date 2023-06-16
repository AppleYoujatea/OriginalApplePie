# 디버깅 이슈


money = int(input())
stocks = list(map(int, input().split()))

def bnp(money, stocks):

    stock = 0
    
    for i in stocks:
        if money >= i:
            # print("money" + str(money))
            # print("i" + str(i))
            stock += money // i
            # print("stock" + str(stock))
            money -= stock * i

    return (money, stock)

def timing(money, stocks):
    streak_up = 0
    streak_down = 0
    yesterday = 0
    stock = 0 

    for i in stocks:
        # print("money" + str(money))
        # print("i" + str(i))
        if i > yesterday:
            streak_up += 1
            streak_up = min(3, streak_up) 
        else:
            streak_up = 0

        if streak_up == 3:
            if money >= i:
                stock += money // i
                money -= stock * i
        
        if i < yesterday:
            streak_down += 1
            streak_down = min(3, streak_down)
        else:
            streak_down = 0
            
        if streak_down == 3:
            money += stock * i
            stock = 0
            
        yesterday = i

    return (money, stock)



bnp_result = bnp(money, stocks)
bnp_money = bnp_result[0] + bnp_result[1] * stocks[-1] 
# print("bnp" + str(bnp_money))
timing_result = timing(money, stocks)
timing_money = timing_result[0] + timing_result[1] * stocks[-1]
# print("timing" + str(timing_money))

if bnp_money > timing_money:
    print("BNP")
elif bnp_money < timing_money: 
    print("TIMING")
else:
    print("SAMESAME")
