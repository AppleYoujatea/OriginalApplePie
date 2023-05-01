import sys

d, b = map(int, input().split())

ds = []
for _ in range(d):
     ds.append(sys.stdin.readline().strip())

bs = []
for _ in range(b):
     bs.append(sys.stdin.readline().strip())

e = list(set(ds).intersection(bs))
e.sort()
print(len(e))
for x in range(len(e)):
    print(e[x])
