import sys
sys.stdin = open("17276.txt", "r")

"""
풀이 시간: 18:30 ~

입력 행렬을 45' 단위로 돌린 행렬 구하기

00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44

00 01 02 03 04 05 06
10 11 12 13 14 15 16
20 21 22 23 24 25 26
30 31 32 33 34 35 36
40 41 42 43 44 45 46
50 51 52 53 54 55 56
60 61 62 63 64 65 66

돌려야 하는 것들

바깥 줄부터 안쪽 줄로
8방향에 있는 요소를 돌려야 함

각도가 0이상이면 시계 방향으로 45'씩
아니라면 반시계 방향으로 45'씩

s,s     s,n/2     s,n
n/2,s   n/2,n/2   n/2,n
n,s     n,n/2     n,n

"""

def rotate_45(matrix, angle):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if angle >= 0:
                new_matrix[i][j] = matrix[n - j - 1][i]
            else:
                new_matrix[i][j] = matrix[j][n - i - 1]
    return new_matrix

T = int(input())

for _ in range(T):
    n, angle = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    angle = angle % 360
    if angle == 0:
        for i in range(n):
            print(*matrix[i])
    else:
        matrix = rotate_45(matrix, angle)
        for i in range(n):
            print(*matrix[i])