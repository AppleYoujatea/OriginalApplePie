"""
풀이 시간: 00:30 ~

누적합 배열 [ {품목1: 누적 개수}, {품목2: 누적 개수}, ... ]
10개씩 건너뛰면서 누적합 배열 탐색하며 -> 구간합 계산
구간합 딕셔너리의 품목별 누적 개수가, number보다 같거나 크면 result += 1
"""

def solution(want, number, discount):   

    result = 0

    # 10개씩 끊어서 품목 개수 count
    for i in range(len(discount) + 1 - 10):
        tmp_arr = discount[i:i+10]
        tmp_dict = {}
        for tmp in tmp_arr:
            if tmp in tmp_dict:
                tmp_dict[tmp] += 1
            else:
                tmp_dict[tmp] = 1

        # 품목 개수 count한 것을 want과 비교
        tmp = 0
        for w in want:
            if w in tmp_dict:
                if tmp_dict[w] >= number[want.index(w)]:
                    tmp += 1

            # 모든 want가 충족되면 cnt
            if tmp == len(want):
                result += 1

    return result

want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
print(solution(want, number, discount))