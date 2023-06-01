import sys
sys.stdin = open("15649.txt", "r")

"""
풀이 시간: 10:43 ~

재귀
빈 배열 생성
함수를 호출:
현재 배열의 길이가 m인지 확인 -> m이면 출력
n만큼 for 문으로 반복
for 문의 현재 원소가 배열에 없다면 추가
재귀적으로 함수를 호출
추가한 원소를 pop()
"""

n, m = map(int, input().split())
ans = []

def check():

    if len(ans) == m:
        print(*ans, sep=" ")
        return

    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            check()
            ans.pop()

check()