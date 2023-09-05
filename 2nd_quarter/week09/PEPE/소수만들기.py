# 에라토스테네스의 체
n = 10 ** 5
eratos_arr = [True for i in range(n+1)]

def eratos():
    for i in range(2, int(n ** 0.5) + 1):
        if eratos_arr[i] == True:
            j = 2
            while i * j <= n:
                eratos_arr[i * j] = False
                j += 1

from itertools import combinations

def solution(nums):
    answer = 0
    eratos()

    combi_list = combinations(nums, 3)

    for combi_elem in combi_list:
        if eratos_arr[sum(combi_elem)] == True:
            answer += 1

    return answer

nums =  [1,2,7,6,4]
print(solution(nums))