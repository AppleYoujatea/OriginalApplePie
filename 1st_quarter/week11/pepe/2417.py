import sys
sys.stdin = open("2417.txt", "r")

"""
풀이 시간: 13:45 ~

이분 탐색
범위: 0부터 n까지

정확히 일치하는 것이 아닌 최솟값을 구하는 문제

탈출 조건을 따로 설정하지 않으면,

"""

n = int(input())

s = 0
e = n

while s <= e:

    mid = (s + e) // 2

    if mid ** 2 < n:
        s = mid + 1
    
    else:
        e = mid - 1

print(s)

# 오른쪽 포인터(e)를 출력하면 안 되는 이유
# while의 조건이 s <= e로 설정했기 때문에, s는 e와 같아질 때까지 진행
# s == e 일 때, while 문은 진행, else 문으로 이동, 마지막 순간에 e -= 1, while 종료
# 따라서 while을 벗어나면, 언제나 s > e인 상태이고, s가 최적값임.