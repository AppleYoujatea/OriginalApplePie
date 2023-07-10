def solution(k, score):
    answer = []
    
    # 상위 k번째 이내일 경우 명예의 전당
    # k일 다음부터는 출연 가수의 점수가 기존 전당 k번째 순위 가수보다 높으면
    # 출연 가수의 점수가 명예의 전당에 오르고 기존의 점수는 내려온다.
    
    arr = []
    for i in range(len(score)):
        if len(arr) < k:
            arr.append(score[i])
        else:
            if score[i] > arr[k-1]:
                arr.pop()
                arr.append(score[i])
    
        arr.sort(reverse=True)
        answer.append(arr[len(arr) - 1])
    
    return answer
