# 반복문 completion 길이만큼
# completion에 있다면 participant에서 제거한다. 효율성테스트 시간초과 실패
# 자료구조로 pop함수 사용해서 시간복잡도 줄일려 했는데 처참히 대실패
# 딕셔너리 쓰면 될듯?
def solution(participant, completion):
    pdict = {}
    cdict = {}

    for i in participant:
        if i in pdict:
            pdict[i] += 1
        else:
            pdict[i] = 1
    for j in completion:
        if j in cdict:
            cdict[j] += 1
        else:
            cdict[j] = 1

    for k in range(len(participant)):
        if participant[k] not in cdict or pdict[participant[k]] != cdict[participant[k]]:
            answer = participant[k]
    return answer