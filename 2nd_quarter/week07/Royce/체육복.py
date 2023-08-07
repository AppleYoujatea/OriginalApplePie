def solution(n, lost, reserve):
    answer = 0
    
    # 가지고 있는데 잃어버리지 않은 것
    set_reserve = set(reserve) - set(lost)
    # 잃어버렸고, 더 가지고 있지 않은 것
    set_lost = set(lost) - set(reserve)
    
    for k in set_reserve:
        if k-1 in set_lost:
            set_lost.remove(k-1)
        elif k+1 in set_lost:
            set_lost.remove(k+1)
    # lost에서 k-1이 있을 경우 있으므로 lost에서 제거
    # k-1에서 없고, k+1의 경우에 있을 경우 k+1에서 제거
    
    # lost 한 것만 제거해주고 크기를 구하면 된다.
    return n - len(set_lost)

    # 1,2,9 가 틀리는 코드
#     arr = [0 for i in range(n+1)]
    
#     for k in range(len(lost)):
#         arr[lost[k]] -= 1
#     for k in range(len(reserve)):
#         arr[reserve[k]] += 1
        
#     for i in range(1,n+1):
#         if arr[i] < 0:
#             if arr[i-1] == 1:
#                 arr[i-1] = 0
#                 arr[i] = 0
#             elif arr[i+1] == 1:
#                 arr[i+1] = 0
#                 arr[i] = 0
    
#     for k in range(1,len(arr)):
#         if arr[k] >= 0:
#             answer += 1
