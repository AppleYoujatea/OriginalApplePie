from collections import Counter
# 풀이 계획
# Counter함수의 사용법을 몰라서 고생했다ㅜ
# want와 number를 딕셔너리화 한 후
# discount를 Counter화 한 것과 값을 비교했다.
# 만약 Counter값이 같다면 answer에 1을 더한다
def solution(want, number, discount):
    answer = 0
    wishList = {}

    for i in range(len(want)):
        wishList[want[i]] = number[i]

    print(wishList)

    for j in range(len(discount) - 9):
        tmp = Counter(discount[j:j + 10])
        if tmp == wishList:
            answer += 1

    return answer

