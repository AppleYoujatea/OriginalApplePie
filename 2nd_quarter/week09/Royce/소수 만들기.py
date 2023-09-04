from itertools import combinations
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
        
    arr = list(combinations(nums, 3))
    for k in arr:
        if is_prime(sum(k)):
            answer+=1
    

    return answer
