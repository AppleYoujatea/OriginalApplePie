import sys
sys.stdin = open("2217.txt", "r")

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

tot = []
for i in range(n):
    tot.append(array[i] * (i + 1))

print(max(tot))