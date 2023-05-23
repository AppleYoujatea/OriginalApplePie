# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
tmp = 0
min_length = sys.maxsize

while True:
    if tmp>= S:
        min_length = min(min_length, right - left)
        tmp -= arr[left]
        left += 1

    elif right == N:
        break

    else:
        tmp += arr[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
