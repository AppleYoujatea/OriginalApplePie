"""
풀이 시간: 20:40 ~

stages를 탐색하면서, 각 스테이지의 실패율을 계산
"""

def solution(N, stages):
    answer = []

    stages_size = len(stages)
    result_dict = {}

    for i in range(1, N + 1): # 1부터 N까지 탐색
        user_count_of_each_stage = stages.count(i)

        if stages_size == 0:
            result_dict[i] = 0
        else:
            result_dict[i] = user_count_of_each_stage / stages_size
        
        stages_size -= user_count_of_each_stage

    return sorted(result_dict, key= lambda x : result_dict[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))