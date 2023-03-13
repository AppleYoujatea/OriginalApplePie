"""
1부터 n까지 배열 생성

n번 만큼 for loop
    pop(k) -> answer.append()
    남은 배열이 1일 때 종료 처리
    다음 인덱스가 배열의 범위를 벗어나지 않게 처리


출력 형식: <elem, elem, elem, ...>
출력은 join가 f string
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [i for i in range(1, n+1)]
answer = []

start = k - 1                               # 시작 위치

for _ in range(n):
    if len(data) == 1:                      # 배열이 1일때 예외 처리
        answer.append(data.pop())
        break

    answer.append(data.pop(start))          # 시작 위치 pop하고 append
    start = (start + k - 1) % len(data)     # 다음 위치로 이동


print(f"<{', '.join(map(str, answer))}>")