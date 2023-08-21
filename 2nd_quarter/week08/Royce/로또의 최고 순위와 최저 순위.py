def solution(lottos, win_nums):
    answer = []
    
    # 당첨 가능한 최고 순위, 최저 순위
    
    num = 0
    cnt = 0
    for k in lottos:
        if k in win_nums:
            num += 1
    # num : 0 제외하고 겹치는 수들
    for k in lottos:
        if k == 0:
            cnt += 1
    if num + cnt == 6:
        answer.append(1)
    elif num + cnt == 5:
        answer.append(2)
    elif num + cnt == 4:
        answer.append(3)
    elif num + cnt == 3:
        answer.append(4)
    elif num + cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if num == 6:
        answer.append(1)
    elif num == 5:
        answer.append(2)
    elif num == 4:
        answer.append(3)
    elif num == 3:
        answer.append(4)
    elif num == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer
