def solution(N, stages):
    answer = []
    
    arr = {}
    num = len(stages)
    
    for k in range(1, N+1):
        if num != 0:
            cnt = stages.count(k)  # stages에서의 k의 개수 구하기
            arr[k] = cnt / num     # arr의 k번째에 cnt/num의 값을 넣어준다.
            num -= cnt             # num에는 남은 cnt를 빼준다.
        else:
            arr[k] = 0             # num이 0이 된 경우 k번째에 0을 넣어준다.
            
    # arr[x]에 대해 정렬을 하는데 내림차순으로 해준다.
    return sorted(arr, key = lambda x: arr[x], reverse=True)
    
