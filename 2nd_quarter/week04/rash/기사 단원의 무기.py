def solution(number, limit, power):
    ## 풀이계획
    ## 반복문으로 약수 개수를 하나씩 구하기 리스트화
    ## 리스트화와 동시에 limit보다 크면 power으로 바꾸기
    ## 리스트 요소의 합 리턴해주기
    answer = 0
    weight = [0] * number
    for i in range(number):
        tmp = getDivisor(i + 1)
        if tmp > limit:
            tmp = power
        weight[i] = tmp
    answer = sum(weight)
    return answer
## 한번 시간초과 되어서 약수 구하는법 인터넷 검색..
def getDivisor(n):
    divisorNum = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0) :
            divisorNum += 1
            if( (i **2) != n):
                divisorNum += 1
    return divisorNum

## 원래 썼었던 함수
def getDivisor2(n):
    divisorNum = 0
    for i in range(1,n):
        if (n % i == 0):
            divisorNum = 1