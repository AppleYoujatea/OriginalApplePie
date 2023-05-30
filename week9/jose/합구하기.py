import sys
# 제일 기본 구간합 개념
# sys.stdin = open("11660.txt", "r")
n = int(input())
arr = list(map(int, input().split()))

sum = [arr[0]]
for i in range(1, n):
    sum.append(sum[i-1] + arr[i])
   
m = int(input())
for i in range(m):
    temp = (list(map(int, sys.stdin.readline().rstrip().split())))
    if temp[0] == 1:
        print(sum[temp[1] - 1])
    else: 
        print(sum[temp[1] - 1] - sum[temp[0] - 2])
