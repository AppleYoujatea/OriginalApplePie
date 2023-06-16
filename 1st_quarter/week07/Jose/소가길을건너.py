import sys 

num = int(input())

cows = {1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7: 2, 8: 2, 9: 2, 10: 2}

count = 0

for i in range(num):
    cow, pos = map(int, sys.stdin.readline().rstrip().split())
    
    if cows[cow] == 2:
        cows[cow] = pos
    else:
        if pos != cows[cow]:
            count += 1
            cows[cow] = pos
    # print(cows)
    # print(count, "  ", cow, " ", pos)

print(count)
