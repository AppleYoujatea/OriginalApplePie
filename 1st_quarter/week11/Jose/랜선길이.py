import sys
ks = []
Knum, N = map(int, input().split())
for _ in range(Knum):
    ks.append(int(sys.stdin.readline()))

start = 1
end = max(ks)

while(start <= end):
    mid = (start + end) // 2
    lines = 0
    for i in ks:
        lines += i // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

        
