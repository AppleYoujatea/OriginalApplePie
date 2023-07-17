def solution(ingredient):
    arr = []
    answer = 0
    for k in ingredient:
        arr.append(k)
        if arr[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                arr.pop()
    return answer
    
