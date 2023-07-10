"""
풀이 시간: 22:44 ~

score의 크기가 작아서 n^2 가능.
-> 새로운 값울 추가할 때마다, 새롭게 정렬해도 괜찮을 듯하다

score 배열을 탐색하면서,
    명전stack의 길이가 k보다 작으면 
        현재 탐색 중인 score의 원소를 stack에 append
    명전stack의 길이가 k보다 같거나 크면
        현재 탐색 중인 score의 원소가, stack의 최솟값보다 크면 
        가장 작은 값 pop()
        현재 탐색 중인 원소 append
    stack을 정렬하고
    가장 작은 값을 result 배열에 append

result 배열을 return 
"""

def solution(k, score):
    answer = []

    stack = []

    for sco in score:
        if len(stack) < k:
            stack.append(sco)
        else:
            if stack[-1] < sco:
                stack.pop()
                stack.append(sco)
        stack.sort(reverse=True)
        answer.append(stack[-1])

    return answer

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k, score))