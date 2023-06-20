def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    
    for idx, i in enumerate(numbers):  
        for j in range(idx+1, len(numbers)):
            if numbers[j] > i:
                answer[idx] = numbers[j]
                break        
    
    return answer
