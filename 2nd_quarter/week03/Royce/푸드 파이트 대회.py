def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        num = food[i] // 2
        for j in range(num):
            answer += str(i)
    
    tmp = answer
    answer += str(0)
    answer += tmp[::-1]
    
    return answer
