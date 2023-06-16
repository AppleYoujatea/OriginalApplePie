a = int(input())
b = list(map(int, input().split()))
c = int(input())


def tired(x, y):
    print(prefix_sum[y] - prefix_sum[x])


nums = []
n = len(b)
prefix_sum = [0] * (n + 1)

for _ in range(c):
    d, f = map(int, input().split())
    nums.append([d, f])

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + b[i]

for z in range(len(nums)):
    first = nums[z][0]
    last = nums[z][-1]
    tired(first - 1, last)
