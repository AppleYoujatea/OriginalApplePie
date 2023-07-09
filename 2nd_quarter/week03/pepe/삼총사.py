"""
풀이 시간: 15:45 ~ 

합이 0이 되면 삼총사
return: 삼총사가 되는 경우의 수

easy -> from itertools import combinations
hard -> 반복문
"""

# hard: 반복문
# def solution(number):

#     arr_size = len(number)
#     result = 0

#     for i in range(arr_size):
#         for j in range(i+1, arr_size):
#             for k in range(j+1, arr_size):
#                 if number[i] + number[j] + number[k] == 0:
#                     result += 1

#     return result

# easy: 조합
from itertools import combinations

def solution(number):
    result = 0

    comb_list = combinations(number, 3)

    for comb_elems in comb_list:
        if sum(comb_elems) == 0:
            result += 1

    return result


number = [-3, -2, -1, 0, 1, 2, 3]
print(solution(number))