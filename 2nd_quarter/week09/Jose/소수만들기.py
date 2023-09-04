def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for idx, i in enumerate(nums):
        for jdx, j in enumerate(nums[idx + 1:]):
            for kdx, k in enumerate(nums[idx + jdx + 2:]):
                if isPrime(i+j+k):
                    answer += 1
    
    return answer
