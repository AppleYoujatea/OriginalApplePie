# 처음 생각 -> 그리디로 최대로 있는 갯수대로 하면 되는거 아님 ? 아님

# 각 점수끼리 최대한으로 묶는 점수 더하기
# 다음에는 나머지 애들에 대해 최대한 상위 애들끼리 묶기
# 그리디 일 수 있는 이유는? 

def solution(k, m, score):
    
    answer = 0
    score.sort(reverse=True)
    temp = []
    for i in score:
        temp.append(i)
        if len(temp) == m:
            answer += min(temp) * m
            temp = []

    return answer
