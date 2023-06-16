import sys
count,price= map(int,input().split())
coinArray = []
coinCount = 0

for i in range(count):
    coinArray.append(int(sys.stdin.readline()))

coinArray.reverse()

for j in range(len(coinArray)):
    coinCount += price // coinArray[j]
    price = price % coinArray[j]
print(coinCount)


