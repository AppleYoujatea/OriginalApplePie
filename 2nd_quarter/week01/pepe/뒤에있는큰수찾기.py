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

    stack = []                      # 뒷큰수를 찾기 위해 대기 중인 인덱스를 저장
    answer = [-1] * len(numbers)    # 정답 배열을 -1로 초기화 -> 갱신되지 않으면 -1

    for i in range(len(numbers)):   # numbers 길이만큼만 반복
        # for문을 반복할 때마다 stack에 쌓여있는 인덱스 친구들을 전부 체크함
        # stack에 맨 위에는, 현재 탐색 중인 인덱스의 직전 인덱스 놓여있음
        # 직전 인덱스가, 현재 인덱스의 값보다 작으면, 뒷큰수 찾은 것 -> 정답 배열 갱신
        # stack이 비어있거나, 현재 인덱스보다 작지 않으면, stack에 현재 인덱스 추가하고 넘어감
        # 뒷큰수를 발견하면, 한 번에 모든 stack을 비울 수 있음
        while stack and numbers[stack[-1]] < numbers[i]: 
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
