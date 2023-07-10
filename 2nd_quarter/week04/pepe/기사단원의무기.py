"""
풀이 시간: 22:57 ~

number 제곱근 범위까지 탐색하면서
    약수의 개수 구함
    약수의 개수가 > limit이면
        power를 result에 append
    아니면
        약수의 개수를 result에 append

result의 합을 return
"""

def solution(number, limit, power):

    answer = 0
    
    for num in range(1, number+1):
        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                cnt += 1

                # 제곱이 되는 약수가 아닌 경우 1를 더 추가
                # 왜냐면 제곱근의 범위만 탐색했기 때문에, 나머지 범위에 또 다른 약수가 있을 것
                if i != num//i:
                    cnt += 1
                    
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer


number = 10
limit = 3
power = 2
print(solution(number, limit, power))