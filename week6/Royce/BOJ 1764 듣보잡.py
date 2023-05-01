
import sys
sys.stdin = open('./work.txt', 'r')
n, m= map(int, input().split())
arr1 = set()
arr2 = set()

for _ in range(n):
    arr1.add(input())
for _ in range(m):
    arr2.add(input())
    
arr = sorted(list(arr1 & arr2))
print(len(arr))

for k in arr:
    print(k)

