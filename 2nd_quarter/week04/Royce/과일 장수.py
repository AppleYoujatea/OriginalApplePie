def solution(k, m, score):
    answer = 0
    
    # 1-k점
    # 한 상자에 사과를 m개씩 담아서 포장
    # 상자에 담긴 사과 중 가장 낮은 점수가 p인 경우, 사과 한 상자의 가격은 p*m
    
    score.sort(reverse=True)
    if len(score) < m:
        return 0
    num = len(score) // m
    
    for i in range(0,len(score)-m+1, m):
        answer += m * score[i+m-1]
    # m m+1 m+2 ... 2m-1
    # 3 3 2 2 1 1 1
    
    return answer
