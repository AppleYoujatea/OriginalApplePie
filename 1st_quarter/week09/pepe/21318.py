import sys
sys.stdin = open("21318.txt", "r")

"""
풀이 시간: 16:10 ~ 16:20 ~ 16:45

시간 제한이 0.5초 -> 누적합을 미리 만들어 두어야
전처리 -> 0번째 인덱스부터 n-1번째 인덱스까지 탐색 -> i와 i+1를 비교해서, i > i+1일 때 1로 기록
누적합 -> 전처리 그래프로 누적합
x번부터 y번까지 연주할 때 -> prefix[j+1] - prefix[i]
"""
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
questions = int(input())

# 전처리 -> 누적합
prefix = [0 for _ in range(n + 1)]
tmp = 0
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        tmp += 1
    prefix[i + 1] = tmp

# prefix[-1] = tmp

# 답 찾기
for _ in range(questions):
    x, y = map(int, input().split())
    # prefix가 입력받은 배열보다 size가 1 크다 -> y-1에서 x-1을 빼주어야 함
    print(prefix[y - 1] - prefix[x - 1])