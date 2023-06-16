a = int(input())
minimalSum = 0
waitList = []

waitList = list(map(int,input().split()))

waitList.sort()
for _ in range(a):
    for a in range(len(waitList)):
        minimalSum += waitList[a]
    waitList.pop()

print(minimalSum)