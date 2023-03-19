a, b = map(int, input().split())

cnt = 0
while True:

    if b <= a:
        break

    if str(b)[-1] == "1":
        b = int(str(b)[:-1])
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        break

if b == a:
    print(cnt + 1)
else:
    print(-1)
