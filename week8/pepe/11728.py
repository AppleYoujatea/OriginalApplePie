import sys
sys.stdin = open("11728.txt")

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

new_arr = arr1 + arr2
new_arr.sort()

print(*new_arr)