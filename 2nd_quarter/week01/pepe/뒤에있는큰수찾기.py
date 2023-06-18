"""
풀이 시간: 16:47 ~

n = 1,000,000 이므로 n^2은 안 됨
뒷 큰 수: 현재 값보다 뒤에 있고 && 큰 숫자

포인터 생성

numbers를 탐색하며, 포인터를 오른쪽으로 이동
이동한 포인터가 현재 값보다 크다면: answer에 추가
작다면: 오른쪽으로 이동
"""


def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer

numbers = [9, 1, 5, 3, 6, 2]	
print(solution(numbers)) 