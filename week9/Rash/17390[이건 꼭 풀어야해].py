nums, questions = map(int, input().split())
prefix_sum = [0] * (nums + 1)
question = []

a = list(map(int, input().split()))
a.sort()


def check(x, y):
    print(prefix_sum[y] - prefix_sum[x])


for i in range(questions):
    b, c = map(int, input().split())
    question.append([b, c])

for j in range(nums):
    prefix_sum[j + 1] = prefix_sum[j] + a[j]

for k in range(questions):
    first = question[k][0]
    last = question[k][-1]

    check(first - 1, last)
