def solution(k, m, score):
    # 계획
    # 역순 정렬
    # 상자개수만큼 리스트화한다
    # 최소값을 구해서 m만큼 곱한걸 answer에 넣는다.
    answer = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i + m]
        if (len(tmp) == m):
            answer += min(tmp) * m
    return answer