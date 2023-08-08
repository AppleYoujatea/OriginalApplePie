"""
풀이 시간: 11:10 ~

r1, r2 = 작은 원, 큰 원
r2를 기준으로 -r2 <= x <= r2, -r2 <= y <= r2 범위를 탐색.
r1 <= 현재 탐색 중인 점의 좌표와 원점 사이의 거리 <= r2의 경우에만 count
"""

import math 

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1) :
        answer += math.floor((r2**2 - i**2)**0.5) - math.ceil(max(0,r1**2 - i**2)**0.5) + 1
    return answer*4

r1 = 2
r2 = 3
print(solution(r1, r2))