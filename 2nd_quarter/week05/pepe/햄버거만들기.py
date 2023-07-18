# 스택?

def solution(ingredient):
    answer = 0

    check = []

    for i in ingredient:
        check.append(i)
        if check[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                check.pop()

    return answer


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]	
print(solution(ingredient))
