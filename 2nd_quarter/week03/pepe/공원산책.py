"""
풀이 시간: 14:30 ~

명령어에 따라 특정 방향+거리 만큼 이동
* 모든 이동이 종료된 이후에 판단하는 것이 아니라, 한 칸 이동할 때마다 판단하는 것임.
모든 명령의 이동이 종료된 이후에, 마지막 위치 return
"""

def solution(park, routes):
    answer = []

    # 시작 좌표 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j

    # 방향
    dir = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}

    # 이동
    for route in routes:
        dx, dy = dir[route.split()[0]]
        n = int(route.split()[1])

        xx, yy = x, y   # 명령 진행 중인 좌표
        canMove = True  # 명령 중간에도, 한 칸 이동할 때마다 가능 여부 확인

        for _ in range(n):
            nx = xx + dx
            ny = yy + dy

            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != "X":
                xx, yy = nx, ny
            else:
                canMove = False
                break

        if canMove:
            x, y = nx, ny
    
    return [x, y]