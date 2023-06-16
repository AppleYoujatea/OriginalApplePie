import sys

# sys.stdin = open("11660.txt", "r")
n, q = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

sum = [arr[0]]
for i in range(1, n):
    sum.append(sum[i-1] + arr[i])

for i in range(q): 
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == 1:
        print(sum[j - 1])
    else: 
        print(sum[j-1] - sum[i-2])
   
