
def solution(park, routes):
    answer = []
    
    # S가 시작, X는 장애물, O는 이동 가능한 통로
    
    x, y = 0, 0
    dir = {"N" : (-1, 0), "S" : (1,0), "W" : (0,-1), "E" : (0,1) }
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
                break
            # 처음 시작 위치를 x,y로 저장한다.
    
    for k in routes:
        direction, num = k.split(" ")
        dx = x
        dy = y
        
        for i in range(int(num)):
            nx = x + dir[direction][0]
            ny = y + dir[direction][1]
            
            if 0<=nx<=len(park) - 1 and 0 <= ny <= len(park[0]) - 1 and park[nx][ny] != "X":
                x = nx
                y = ny
            # 범위 안에 있고, X가 아닌 경우에만 옮긴다.
                
            else:
                x = dx
                y = dy
                break
            # 아닌 경우 x,y를 dx,dy로 놓고 끝낸다.
    
    
    return (x, y)
