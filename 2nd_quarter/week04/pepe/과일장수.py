"""
풀이 시간: 23:37 ~

그냥 정렬해서 m개씩 자르면 될 듯?
정렬은 내림차순으로 해서, 자르고 남은 것을 버릴 때 최소를 버릴 수 있게

sorted_score = sorted(score, reverse=True)

result = []

for i in range(-1, len(sorted_score), m):
    result.append(sorted_score[i:i+m])

return result
"""

def solution(k, m, score):

    answer = 0

    result = []
    sorted_score = sorted(score, reverse=True)

    for i in range(0, len(sorted_score) + 1, m):
        result.append(sorted_score[i:i+m])

    for res in result:
        if len(res) == m:
            answer += res[-1] * m

    return answer

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
print(solution(k, m, score))
