def solution(name, yearning, photo):
    ## 1 사진 안에 사람들의 이름이 있는지 확인한다
    ## 2. 만약 있다면 사진안에 이름이 있다면 그사람들의 점수가 있는지 확인
    ## 3. 만약 그사람의 점수가 있다면 더한다.

    answer = []
    Scores = dict(zip(name, yearning))
    for i in range(len(photo)):
        scoreSum = 0
        for j in name:
            if j in photo[i]:
                scoreSum += Scores[j]
        answer.append(scoreSum)

    return answer