"""
풀이 시간: 23:58 ~

dict1 = { 유저ID : set(유저가 신고한 ID) }
dict2 = { 유저ID : set(나를 신고한 ID) }

dict1을 탐색하며 유저가 신고한 ID를 key로 dict2에서 value의 길이를 확인.
value의 길이가 k 이상이면 tmp += 1
result 배열에 tmp 기록
"""

from collections import defaultdict

def solution(id_list, report, k):

    dict1 = defaultdict(set)
    dict2 = defaultdict(set)

    for rep in report:
        user, target = rep.split()
        dict1[user].add(target)
        dict2[target].add(user)

    result = []
    for user in id_list:
        tmp = 0
        for target in dict1[user]:
            if len(dict2[target]) >= k:
                tmp += 1
        result.append(tmp)

    return result

    

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))