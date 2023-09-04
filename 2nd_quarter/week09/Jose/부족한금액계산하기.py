def solution(price, money, count):
    answer = -1
    counts = 0 
    for i in range(count+1):
        counts += i
        
    if money >= counts * price:
        answer = 0
    else: 
        answer = counts * price - money

    return answer
