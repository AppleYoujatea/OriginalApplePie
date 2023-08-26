# 풀이계획
# 1. 숫자를 정렬한다.
# 2. 숫자를 정렬 후 tmp를 만들어 budget과 비교
# 3. tmp가 budget보다 커지거나 같으면 중단 동시에 answer += 1
def solution(d, budget):
    answer = 0
    tmp = 0
    d.sort()
    for i in range(len(d)):
        tmp += d[i]
        if tmp <= budget:
            answer += 1
            
        else:
            break
        
    return answer