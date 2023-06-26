"""
풀이 시간: 22:15 ~

today_year, today_month, today_day = today.split(".")
terms_dict = [{term : int(term_date)} for term, term_date in terms.split()]

privacies에는 [개인정보 수집일자, 약관 종류]

answer = []
for i in range(len(privacies))
    if 오늘 날짜 < 개인정보 수집일자 + 약관 종류:
        answer.append(현재인덱스 + 1)
"""


def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = map(int, today.split("."))
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}

    for i in range(len(privacies)):
        privacy_date, privacy_term = privacies[i].split()
        privacy_year, privacy_month, privacy_day = map(int, privacy_date.split("."))
        
        # privacy_month + terms_dict[privacy_term] => 12라면, 단순 12로 나눈 나머지를 구했을 때 0이 나옴
        # 그래서 privacy_month - 1 + terms_dict[privacy_term]이라면, 계산 결과가 11이 나오고, 12로 나눈 나머지를 구하고 1을 더하면 12가 됨
        expiration_month = (privacy_month - 1 + terms_dict[privacy_term]) % 12 + 1
        expiration_year = privacy_year + (privacy_month - 1 + terms_dict[privacy_term]) // 12

        if (today_year, today_month, today_day) >= (expiration_year, expiration_month, privacy_day):
            answer.append(i + 1)
    
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))