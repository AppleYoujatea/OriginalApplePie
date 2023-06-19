S = int(input())
sum = 0
N = 0
for i in range(1, S+1):
    if sum < S:
        sum += i
        N += 1
    else:
        break

if sum == S:
    print(N)
else: 
    print(N-1)
