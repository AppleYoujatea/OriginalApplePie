
import itertools


def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    candidates = list(itertools.product(sales, repeat=len(emoticons)))

    ans = []
    for candi in candidates:  # candi = [10, 10, 20, 40]
        candi_tmp = [0, 0]
        for user in users:
            user_tmp = [0, 0]  # [톡플러스 가입, 금액]

            for i in range(len(candi)):
                if user[0] <= candi[i]:  # user가 정한 할인율 이상
                    # 금액에 더해줌
                    user_tmp[1] += emoticons[i] * ((100 - candi[i])) / 100

            if user[1] <= user_tmp[1]:  # user가 정한 금액 이상
                user_tmp[0] = 1  # 톡플러스 가입
                user_tmp[1] = 0  # 가입 후 구매 취소

            # 해당 candi 리스트에 값 더해줌
            candi_tmp[0] += user_tmp[0]
            candi_tmp[1] += user_tmp[1]

        # candi 하나 반복 끝나면, 정답 리스트에 append
        ans.append(candi_tmp)

    # 톡플러스 가입자 수 -> 금액 순으로 정렬
    ans.sort(key=lambda x: (x[0], x[1]))
    return ans[-1]
