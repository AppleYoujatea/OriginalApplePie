import sys
sys.stdin = open("2470.txt", "r")

"""
풀이: 16:31 ~ 17:05

정렬하고, 투 포인터로 양쪽에서 가운데 방향으로 탐색
while i < j

현재 값보다 abs(sum)이 작으면 기록

sum이 음수 -> 왼쪽 포인터를 오른쪽으로
sum이 양수 -> 오른쪽 포인터를 왼쪽으로
"""

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

i = 0
j = n - 1

answer_sum = abs(num_list[i] + num_list[j])
answer_list = [num_list[i], num_list[j]]


while i < j:
    left = num_list[i]
    right = num_list[j]
    tmp_sum = left + right

    if abs(tmp_sum) < answer_sum:
        answer_sum = abs(tmp_sum)
        answer_list = [left, right]

        if answer_sum == 0:
            break

    if tmp_sum < 0:
        i += 1
    else:
        j -= 1

print(*answer_list)