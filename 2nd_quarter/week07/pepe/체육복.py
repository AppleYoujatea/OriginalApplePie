"""
풀이 시간: 21:25 ~

그대로 구현하되 순서를 정해보자
0. 각 학생이 갖고 있는 체육복의 개수를 보여주는 배열 선언
1. reserve 더하기
2. lost 빼기
3. 배열을 탐색하며, 양쪽에 빈 곳이 있다면 나눠주기
"""

def solution(n, lost, reserve):

    # 길이가 n인 리스트(now)를 1로 초기화한다 (체육복을 갖고 있다고 가정)
    now = [1] * (n + 2)
    # now = [1, 1, 1, 1, 1, 1, 1]
    # idx =  0, 1, 2, 3, 4, 5, 6

    # reverse 리스트를 탐색하며, 해당 인덱스에 체육복을 1개 더해준다.
    for r in reserve:
        now[r] += 1  # now = [1, 2, 1, 2, 1, 2]

    # lost 리스트를 탐색하며, 해당 인덱스에 체육복을 1개 빼준다.
    for l in lost:
        now[l] -= 1  # now = [1, 2, 0, 2, 0, 2]

    # now 리스트를 탐색하며,
    for i in range(1, len(now)):
        # 현재 item이 2이고,
        if now[i] == 2:

            # 왼쪽이 0이면
            if now[i - 1] == 0:
                # # 현재 item을 1 빼고, 인접한 item에 1 더해준다.
                now[i] -= 1
                now[i - 1] += 1

            # 오른쪽이 0이면
            elif now[i + 1] == 0:
                # # 현재 item을 1 빼고, 인접한 item에 1 더해준다.
                now[i] -= 1
                now[i + 1] += 1
        else:
            continue

    # now 리스트 탐색이 종료
    # now = [1, 1, 1, 1, 1, 2, 1]

    answer = 0
    for i in range(1, len(now) - 1):
        if now[i]:
            answer += 1
        else:
            pass

    return answer