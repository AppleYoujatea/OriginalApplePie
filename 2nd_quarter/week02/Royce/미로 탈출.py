def solution(wallpaper):
    answer = []
    
    Minx = 9999
    Miny = 9999
    Maxx = 0
    Maxy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if Minx >= i:
                    Minx = i
                if Miny >= j:
                    Miny = j
                if Maxx <= i+1:
                    Maxx = i+1
                if Maxy <= j+1:
                    Maxy = j+1
            
    answer.append(Minx)
    answer.append(Miny)
    answer.append(Maxx)
    answer.append(Maxy)
    
    return answer
