# 풀이계획
# 1번 먼저 n번째 문자를 기준으로 단어를 정렬 -> 이중배열로 변경
# 느낀점 파이썬 람다는 개사기다

def solution(strings, n):
    b = []
    answer = []
    for i in range(len(strings)):
        tmp = strings[i]
        b.append([strings[i], tmp[n]])

    b.sort(key=lambda x: (x[1], x[0]))
    for i in range(len(b)):
        answer.append(b[i][0])

    return answer
