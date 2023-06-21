"""
풀이 시간: 16:30 ~

한 번 칠했을 때, 롤러의 길이만큼 칠하게 됨
칠했을 때, 현재 위치 - 이전 위치 >= 롤러의 길이라면, 다시 칠해야 하므로, cnt += 1, 위치 이동
"""

def solution(n, m, section):

    now = section[0]
    cnt = 1 # 최소 1번 칠하고 시작

    for i in range(1, len(section)):
        if section[i] - now >= m: # 한 번의 색칠로 m-1 길이의 범위만큼 덧칠
            cnt += 1
            now = section[i]

    return cnt

n = 8
m = 4
section = [2, 3, 6]
print(solution(n, m, section))