"""
풀이 시간: 17:11 ~

0을 포함한 로또 번호가 주어짐
win_nums와 비교하여, 0을 수정했을 때, 최고 순위와 최저 순위를 return

순서는 상관X

일단 직관적으로 생각나지는 않음 ...

집합으로 풀이
base = lottos와 win_nums에서 중복되는 숫자의 개수
base + 0의 개수 => 가장 높은 순위
base => 가장 낮은 순위

순위를 구하는 방법은 
rank = 7 - 일치하는 개수
rank가 6, 7이면 6으로 통일
"""

def solution(lottos, win_nums):
    answer = []

    base = set(lottos) & set(win_nums)
    cnt_zero = lottos.count(0)

    upper_rank = min(6, 7 - (len(base) + cnt_zero))
    lower_rank = min(6, 7 - len(base))

    return [upper_rank, lower_rank]

lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]
print(solution(lottos, win_nums))