import sys
count = int(sys.stdin.readline())
lope_list = []
for i in range(count):
    lope_list.append(int(input()))
lope_list.sort()

res = 0
king = []

for i in range(len(lope_list)):
    king.append(lope_list[i] * count)
    count -= 1

res = max(king)


print(res)