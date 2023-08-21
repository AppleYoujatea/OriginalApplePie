import math
def solution(n):
    answer = 0
    for i in range(2,n + 1):
        answer += 소수판별(i)
    return answer


def 소수판별(x):
    for i in range (2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return 0
    return 1