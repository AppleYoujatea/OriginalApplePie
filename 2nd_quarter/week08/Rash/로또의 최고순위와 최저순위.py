# 풀이계획 
# 1. 0의 개수 파악
# 2. 똑같은 숫자 파악
# 3. 똑같은 숫자 + 0의 개수로 최대 등수 정하기
# 4. 똑같은 숫자로 최소 등수 정하기
def solution(lottos, win_nums):
    changer = lottos.count(0)
    same = 0
    maxcnt = 0
    mincnt = 0
    answer = []
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            same += 1
    maxcnt = same + changer
    mincnt = same
    
    answer.append(prize(maxcnt))
    answer.append(prize(mincnt))
    return answer
            
            

def prize(samecnt):
    if samecnt == 6:
        return 1
    elif samecnt == 5:
        return 2
    elif samecnt == 4:
        return 3
    elif samecnt == 3:
        return 4
    elif samecnt == 2:
        return 5
    elif samecnt <= 1:
        return 6