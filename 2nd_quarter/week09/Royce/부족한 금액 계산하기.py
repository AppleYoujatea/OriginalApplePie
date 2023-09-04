def solution(price, money, count):
    answer = 0
    
    tmp = price
    for i in range(count):
        answer += price
        price += tmp
    
    if answer - money < 0:
        return 0

    return answer - money
