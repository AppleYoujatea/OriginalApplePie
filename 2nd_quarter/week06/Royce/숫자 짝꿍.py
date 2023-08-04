def solution(X, Y):
    answer = []
    
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    # X에서의 i개수와 Y에서의 i개수 중 작은 값에 대한 횟수 만큼 answer에 i를 넣어준다.
    
    answer.sort(reverse=True)
    
    # 아예 없을 경우에 -1을 리턴한다.
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    # 정렬을 했는데도 제일 앞에 있는게 0일 경우 그냥 0을 리턴한다.
    
    answer = "".join(answer)
    
    
    
    return answer
