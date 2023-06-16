fir, fin = map(int, input().split())
count = 1

while True:
    if fir > fin:
        count = -1
        break
    elif fir == fin:
        break
    elif fin % 10 == 1:
        fin = fin // 10
        count += 1
    elif fin % 2 == 0:
        fin = fin // 2
        count += 1
    else:
        count = -1
        break

print(count)
