# 풀이 계획
# 반복문을 통해서  1,2,3,1 의 순서를 가진 리스트가 있는지 찾는다
# 만약 있다면 그 요소들을 remove한다 answer에1을 더한다.
# 다시 반복문을 통해 찾음 만약 없다면 return

def solution(ingredient):
    tmp = []
    answer = 0
    recipe = [1,2,3,1]
    i = 0
    while(True):
        tmp = ingredient[i:i+4]
        if tmp == recipe:
            answer += 1
            del ingredient[i:i+4]
            if i - 3 <= 0:
                i = 0
            else:
                i -= 3
        elif i >= len(ingredient):
            break
        else:
            i += 1
    print(recipe)

    return answer