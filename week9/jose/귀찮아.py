# 모든 것은 수학이다.

n = int(input())
input = list(map(int, input().split()))

# x2 + x3 + .. xn
total_sum = sum(input)
sum = [total_sum]

for i in range(n): 
    sum.append(sum[i]-input[i])

# what i need is x2+x3+x4+...xn, x3+x4+..xn, 
# sum[1] is for the first input

result = 0
for i in range(n):
    result += input[i]*sum[i+1]
print(result)

