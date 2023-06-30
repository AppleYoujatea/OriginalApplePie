"""
풀이 시간: 15:25 ~

펠린드롬을 return
대칭이 되는 짝수 개의 숫자만 사용

food 배열을 탐색
size = 1번째 인덱스부터 2로 나눈 몫만 사용
현재 인덱스 * size 만큼 tmp 문자열에 더하기
food 배열 탐색이 끝나면, "0", 기존 문자열[::-1]을 더하기
"""

def solution(food):
    answer = ""

    for i in range(1, len(food)):
        size = food[i] // 2
        answer += str(i) * size

    tmp = answer
    answer += "0"
    answer += tmp[::-1]

    return answer

food = [1, 3, 4, 6]
print(solution(food))