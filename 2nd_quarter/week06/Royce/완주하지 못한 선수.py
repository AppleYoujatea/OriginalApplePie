def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    if len(participant) == 1:
        return participant[0]

    for i in range(0, len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break   # 다를 경우 answer이다.
        else:
            answer = participant[i+1]
            # 같을 경우 그 다음 부분으로 넘기고 다음 진행
            # 더 없을 경우 그때는 이것이 답이 되는 것이다..
            
            # 한명을 찾는 것이므로 answer에 participant를 다음으로 넘기면서 찾아줄 수 있는 것이다.
    
    return answer
