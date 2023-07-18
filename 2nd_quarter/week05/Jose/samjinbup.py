def solution(n):
    answer = 0
    quotient = "" 
    
    while n >= 3:
        quotient += str(n % 3)
        n = n // 3
    quotient += str(n)
    
    for num, i in enumerate(quotient):
        answer += int(i) * (3** (len(quotient) - num - 1))
    
    return answer
