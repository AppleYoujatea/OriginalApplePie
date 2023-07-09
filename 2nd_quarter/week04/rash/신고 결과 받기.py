def solution(id_list, report, k):
    # 계획
    # 신고한 사람을 저장하는 딕셔너리 생성
    # 신고당한 횟수를 저장하는 딕셔너리 생성
    # 중복 신고 제외
    # 신고 횟수가 k를 넘으면 answer리스트 +1
    answer = [0] * len(id_list)
    arrcnt = {}
    repcnt = {}
    for i in range(len(id_list)):
        arrcnt[id_list[i]] = 0
        repcnt[id_list[i]] = []

    processed_reports = set()

    for i in report:
        tmp = i.split(" ")
        reporter = tmp[0]
        reported = tmp[1]

        if i in processed_reports:
            continue

        processed_reports.add(i)

        if reported in arrcnt:
            arrcnt[reported] += 1
            repcnt[reporter].append(reported)

    for i in range(len(id_list)):
        reported_users = repcnt[id_list[i]]
        for user in reported_users:
            if arrcnt[user] >= k:
                answer[i] += 1

    return answer


## 개쩐다고 생각한 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {}
    for x in id_list:
        reports[x] = 0

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer