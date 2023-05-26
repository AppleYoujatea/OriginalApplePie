import sys
sys.stdin = open("11660.txt", "r")

"""
풀이 시간: 16:50 ~ 17:10

누적합 x1,y1 ~ x2,y2 = sum_arr[x2 + 1][y2 + 1] - sum_arr[x1][y2 + 1] - sum_arr[x2 + 1][y1] + sum_arr[x1][y1]
"""
import sys
input = sys.stdin.readline

n, tc = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 누적합 그래프
sum_arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = arr[i - 1][j - 1] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j -1]

# 구간 더하기
# 입력 좌표에서 -1 해주는 것 유의
for _ in range(tc):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1]
    print(result)