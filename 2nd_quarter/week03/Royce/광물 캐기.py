def solution(picks, minerals):
    answer = 0
    
    #     다이아 철 돌
    # 다이아 1   1  1
    #  철   5   1  1
    #  돌  25   5  1
    
    # 사용할 수 있는 곡괭이 중 아무거나 하나를 선택
    # 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용
    # 주어진 순서대로만 가능
    
    num = 0
    for k in picks:
        num += k
        
    gok = num * 5
    
    # minerals의 배열의 개수가 num보다 많을 경우 캘 수 있는 만큼만 자른다.
    if len(minerals) > num:
        minerals = minerals[:gok]
    
    next = [[0,0,0] for _ in range((len(minerals) // 5 + 1))]
    # 다음 광물을 위해서 배열을 만들어준다.
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            next[i // 5][0] += 1
        elif minerals[i] == 'iron':
            next[i // 5][1] += 1
        elif minerals[i] == 'stone':
            next[i // 5][2] += 1
        # 다이아인 경우, 철, 돌인 경우 각각 1씩 더한다.
    
    next.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    # 다이아몬드, 철, 돌 순서로 정렬한다.
    
    for k in next:
        diamond, iron, stone = k
        
        for t in range(len(picks)):
            if picks[t] > 0 and t == 0:
                picks[t] -= 1
                answer += diamond + iron + stone
                break
            elif picks[t] > 0 and t == 1:
                picks[t] -= 1
                answer += (5 * diamond) + iron + stone
                break
            elif picks[t] > 0 and t == 2:
                picks[t] -= 1
                answer += (25 * diamond) + (5 * iron) + stone
                break
                
    
    return answer
