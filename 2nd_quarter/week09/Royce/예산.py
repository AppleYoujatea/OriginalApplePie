def solution(d, budget):
    answer = 0
    
    d.sort()
    
    num = budget
    for k in d:
        if num >= k:
            num -= k
            answer += 1
        else:
            return answer
        
    return answer



# def solution(d, budget):
#     answer = 0
    
#     arr = sorted(d)
#     num = 0
#     for k in arr:
#         if num + k <= budget:
#             num += k
#             answer+=1
#         else:
#             break
    
    
#     return answer
