count = int(input())
difficulty = list(map(int, input().split()))
question = int(input())

nums = []
n = len(difficulty)
fail = 0
prefix_sum = [0] * n


def check(x, y):
    print(prefix_sum[y] - prefix_sum[x])


for _ in range(question):
    a, b = map(int, input().split())
    nums.append([a, b])

for i in range(n - 1):
    if difficulty[i] > difficulty[i + 1]:
        fail += 1
    prefix_sum[i + 1] = fail

for j in range(question):
    first = nums[j][0]
    last = nums[j][-1]
    check(first - 1, last - 1)
