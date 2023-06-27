def solution(n, m, section):
    answer = 0

    while len(section) > 0:
        current = section[0]
        for i in range(m):
            if current == section[0]:
                section.pop(0)
                if len(section) == 0:
                    break
            current += 1
        answer += 1

    return answer
