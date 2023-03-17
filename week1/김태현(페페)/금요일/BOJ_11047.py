n, m = map(int, input().split())
array = []
tot = 0

for _ in range(n):
    array.append(int(input()))

    
cnt = -1
while m:
    tot += m // array[cnt]
    m %= array[cnt]
    cnt -= 1
    
