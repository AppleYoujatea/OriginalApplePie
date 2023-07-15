# 풀이계획
# 1. 주어진 n을 10진법에서 3진법의 수로 바꾼다.
# 2. 3진법의 수를 뒤집는다.
# 3. 다시 3진법으로 바꾼다.
# 파이썬 기본라이브러리는 생각보다 더 개꿀이다.

def solution(n):
    tmp = ''
    base = 3
    reversetmp = ""
    answer = 0
    while n:
        tmp = str(n % base) + tmp
        n = n // base

    for i in range(len(tmp)):
        reversetmp += tmp[-i - 1]

    answer = int(reversetmp, 3)
    return answer