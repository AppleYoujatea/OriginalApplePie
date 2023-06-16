import sys
sys.stdin = open("BOJ_11399.txt", "r")

# 오름차순 정렬
# for loop: i는 1부터 n까지
# for loop: j는 1부터 i까지 -> tot += array[j]

n = int(input())
array = list(map(int, input().split()))

array.sort()

tot = 0
for i in range(1, n+1):
    for j in range(i):
        tot += array[j]

print(tot)

