def solution(today, terms, privacies):
    answer = []
    time_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])

    for i in terms:
        case = terms[0]
        time_dict[case] = int(terms[2:])

    for j in range(len(privacies)):
        date, case = privacies[j].split()
        p_year, p_month, p_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])

        p_month += time_dict[case]

        while p_month > 12:
            p_month -= 12
            p_year += 1

        if p_year > year:
            continue

        elif p_year == year:
            if p_month > month:
                continue

            elif p_month == month:
                if p_day > day:
                    continue

        answer.append(i + 1)
        # 배열사용을 위해 i는 0부터 시작하므로 정답에 +1 하여 추가합니다
        # print(p_year,p_month,p_day,case)

        return answer


