def solution(ingredient):
    
    spare = []
    perfect = [1,2,3,1]
    answer = 0
    
    for i in ingredient:
        spare.append(i)
        if len(spare) >= 4:
            if spare[len(spare)-4:len(spare)] == perfect:
                spare.pop()
                spare.pop()
                spare.pop()
                spare.pop()
                answer += 1
                
    return answer
