num = int(input())
numbers = list(map(int, input().split()))

dp = [1 for _ in range(num)]


for n, i in enumerate(numbers):
    temp = []
    for j in range(n):   
        if i > numbers[j]:
            temp.append(dp[j])
    if temp:
	    dp[n] = max(temp) + 1
        
print(max(dp))
