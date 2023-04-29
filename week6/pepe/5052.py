import sys
sys.stdin = open("5052.txt", "r")

"""
풀이 시간: 13 : 02 ~ 13 : 15 ~ 13 : 16

.startwith() 쓰는 문제인 듯
그냥 n ** 2완탐하면 시간초과 날 것 같음 10 ** 4 ** 2
정렬하고 선형 탐색으로 고고 ----> 정렬하면 바로 뒤에만 확인하면 됨

data = 입력값을 모두 받은 리스트
data 길이 오름차순으로 정렬

data를 선형 탐색하며
짧은 것
"""

tc = int(input())

for _ in range(tc):

    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    flag = True

    for i in range(n - 1):
        size = len(nums[i])

        if nums[i] == nums[i + 1][:size]:
            flag = False

    if flag:
        print("YES")
    else:
        print("NO")