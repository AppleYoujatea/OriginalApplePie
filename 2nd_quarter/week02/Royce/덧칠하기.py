def solution(n, m, section):
    answer = 0
    num = 0
    
    for k in section:
        if k > num:
            num = k + m - 1
            answer += 1
    
    
    return answer
