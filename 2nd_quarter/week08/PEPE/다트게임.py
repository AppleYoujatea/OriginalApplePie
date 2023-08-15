"""
풀이 시간: 17:32 ~

점수마다 *, # 존재할 수 있음
*이 나오면, 이전 점수와 현재 점수 2배
#이 나오면, 현재 점수 -1배

10은 헷갈리니까 다른 숫자로 변경하는 게 나을 듯 ex) 0

각 회차마다 값을 계산해서 result에 담아두고 마지막에 sum해서 return 하는 게 나을 듯.
*이 나오면 바로 앞 회차의 점수를 2배 해주어야 하기 때문에

darResult를 탐색하면서, 숫자를 기준으로 끊어 tmp 변수에 담고, 점수를 계산해서 result에 append
숫자 기준으로 끊을 때는, 주어진 문자열이 숫자로 되어있는지 검사하는 .isdigit() 사용하기
"""

def solution(dartResult):
    score = []
    i = 0

    while i < len(dartResult):
        # 10 처리
        if dartResult[i] == '1' and dartResult[i + 1] == '0':
            dartResult_to_int = 10
            i += 1
        else:
            dartResult_to_int = int(dartResult[i])

        i += 1

        if dartResult[i] == 'S':
            score.append(dartResult_to_int)
        elif dartResult[i] == 'D':
            score.append(dartResult_to_int**2)
        elif dartResult[i] == 'T':
            score.append(dartResult_to_int**3)

        i += 1
        
        if i < len(dartResult) and dartResult[i] == '*':
            if len(score) >= 2:
                score[-2] *= 2
            score[-1] *= 2
            i += 1
            
        elif i < len(dartResult) and dartResult[i] == '#':
            score[-1] *= -1
            i += 1
            
    return sum(score)


dartResult = "1D2S#10S"
print(solution(dartResult))