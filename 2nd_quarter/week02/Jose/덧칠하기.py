
def solution(n, m, section):

    cnt = 0
    idx = 0 
    r = 0 
    
    # 깨달음 ! 시작을 0부터 할 필요가 없다는 사실을 
    while idx < len(section):
        # print(r, section[idx])
        if r < section[idx]:
            r = section[idx] + m - 1
            cnt +=1
        idx += 1 

    return cnt
