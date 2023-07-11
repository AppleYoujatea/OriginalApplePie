def solution(k, score):
    answer = []
    board = []
    
    for i in range(1, len(score)+1):
        temp = score[:i]
        temp.sort(reverse=True)
        
        if len(temp) < k:
            answer.append(temp[-1])
        else:
            answer.append(temp[k-1])
    
    return answer

