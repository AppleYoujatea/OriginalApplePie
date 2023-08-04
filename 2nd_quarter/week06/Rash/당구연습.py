# 풀이 게획
# 1. 같은 x축에 있다면 무조건 y축을 이용해야한다.  y축 반전 두개만 구하고 그중에서 최솟값을 구하면 된다.
# 2. 같은 y축에 있다면 무조건 x축을 이용해야한다.  x축 반전 두개만 구하고 그중에서 최솟값을 구한다.
# 3. 만약 둘다 동일선상에 없다면 1,2,3,4 전부 구하고 최솟값을 구하면 되지 않을까?


import math


def solution(m, n, startX, startY, balls):
    answer = []
    for i in range(len(balls)):
        X = startX
        Y = startY

        Top = (balls[i][0] - X) ** 2 + (balls[i][1] - (Y + 2 * (n - Y))) ** 2
        Bottom = (balls[i][0] - X) ** 2 + (balls[i][1] + Y) ** 2
        Left = (balls[i][0] + X) ** 2 + (balls[i][1] - Y) ** 2
        Right = (balls[i][0] - (X + 2 * (m - X))) ** 2 + (balls[i][1] - Y) ** 2

        if startX == balls[i][0] and startY > balls[i][1]:
            distance = min(Left, Right, Top)

        elif startX == balls[i][0] and startY < balls[i][1]:
            distance = min(Left, Right, Bottom)

        elif startY == balls[i][1] and startX > balls[i][0]:
            distance = min(Top, Bottom, Right)

        elif startY == balls[i][1] and startX < balls[i][0]:
            distance = min(Top, Bottom, Left)

        else:
            distance = min(Top, Bottom, Left, Right)

        answer.append(distance)

    return answer
