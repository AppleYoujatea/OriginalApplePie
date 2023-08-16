# 번호 일치하는 것만 계산해서 최저 
# 번호 일치 + 0 인 것 계산해서 최대
def solution(lottos, win_nums):
    answer = []
    low = 0
    high = 0 
    for lotto in lottos:
        if lotto in win_nums:
            low += 1
        elif lotto == 0: 
            high += 1 
    high += low
    
    if high == 0:
        high = 1
    if low == 0:
        low = 1 
        
    return [(7 - high), (7 - low)]
