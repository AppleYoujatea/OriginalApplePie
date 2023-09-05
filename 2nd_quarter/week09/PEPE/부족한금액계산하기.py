def solution(price, money, count):
    tot = 0

    for i in range(1, count+1):
        tot += price * i
        
    answer = tot - money

    return answer if answer >= 0 else 0