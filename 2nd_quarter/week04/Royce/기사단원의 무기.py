import math
def find(num):
    cnt = 2
    if math.sqrt(num) == int(math.sqrt(num)):
        cnt -= 1
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            cnt += 2
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        if find(i) <= limit:
            answer += find(i)
        else:
            answer += power
    

    return answer
