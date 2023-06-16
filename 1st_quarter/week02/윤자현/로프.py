import sys

n = int(input())

lope = []
for i in range(n):
  a = int(sys.stdin.readline())
  lope.append(a)

lope.sort()

maximum = 0

for num, i in enumerate(lope):
  temp = min(lope[num:]) * (n - num)
  if maximum < temp:
    maximum = temp
  else:
    break

print(maximum)
