def whichStep(direction):
    value = (0, 0)
    if direction == "N":
        value = (-1, 0)
    elif direction == "S":
        value = (1, 0)
    elif direction == "W":
        value = (0, -1)
    else: 
        value = (0, 1)
    return value

def solution(park, routes):
    answer = []
    
    width = len(park)
    height = len(park[0])
    
    start = tuple()
    
    for inum, i in enumerate(park):
        for jnum, j in enumerate(i):
            if j == "S":
                start = (inum, jnum)
    
    park_copy = park
    current = start
    
    for i in routes:
        direction, step = i.split()
        direction = whichStep(direction)
        temp = current
        valid = True 
        
        for j in range(int(step)):
            temp = (temp[0] + direction[0], temp[1] + direction[1])
            if temp[0] == width or temp[1] == height or temp[0] < 0 or temp[1] < 0:
                valid = False
                break
            elif park_copy[temp[0]][temp[1]] == "X":
                valid = False
                break
                
        if valid:
            current = temp
        
    return current

    
    
    
