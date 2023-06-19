"""
풀이 시간: 00:37 ~ 

dic = {uuid : name}
msg = []

enter 혹은 leave 메시지는, 
1. [명령어, uuid] 형식으로 msg에 저장

enter 혹은 change 메시지는,
1. dic의 uuid에 해당하는 value를 갱신

record 탐색 끝나면 전부 출력
"""

from collections import defaultdict

def solution(record):
    answer = []

    msg = []
    dic = defaultdict(str)

    for rec in record:

        order = list(rec.split())

        if order[0] == "Enter" or order[0] == "Leave":
            msg.append([order[0], order[1]])
        
        if order[0] == "Enter" or order[0] == "Change":
            dic[order[1]] = order[2]

    for m in msg:
        if m[0] == "Enter":
            answer.append(f"{dic[m[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[m[1]]}님이 나갔습니다.")

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))