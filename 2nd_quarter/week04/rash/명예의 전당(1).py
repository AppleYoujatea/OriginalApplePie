def solution(k, score):
    # 풀이계획
    # 빈 리스트를 생성한다.,
    # 리스트 내림차순 정렬후 리스트의 크기가 k보다 작으면 마지막 값을 answer에 추가한다.그리고 계속 score값을 리스트에 추가
    # 만약 리스트가 k보다 커지면 정렬후 마지막 값을 answer에 추가후 리스트를 Pop한다.
    # 계속 score를 추가해주고 스코어의 하나를 pop해준다.
    answer = []
    honor = []
    for i in range(len(score)):
        a = -1
        honor.append(score[i])
        honor.sort(reverse=True)
        tmp = honor[a]
        if len(honor) > k:
            a = k - 1
            tmp = honor[a]
            honor.pop()
        answer.append(tmp)

    return answer