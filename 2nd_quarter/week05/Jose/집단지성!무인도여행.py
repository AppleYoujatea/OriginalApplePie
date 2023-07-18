import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))] 
    
    def DFS(x, y, val):
        
        visited[x][y] = 1
        if maps[x][y] != "X":
            val += int(maps[x][y])
                
        if (x>0):
            if (visited[x-1][y] ==0 and maps[x-1][y] != "X" ):
                val = DFS(x-1, y,val)     
        if (y>0): 
            if (visited[x][y-1]==0 and maps[x][y-1]!= "X"):
                val = DFS(x,y-1, val)
        if (x<len(maps)-1 and maps[x+1][y] != "X"): 
            if (visited[x+1][y]==0):
                val = DFS(x+1,y, val)     
        if (y<len(maps[0])-1 and maps[x][y+1] !="X"):
            if (visited[x][y+1]==0):
                val = DFS(x,y+1, val)
            
        return val
    
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j] == 0 and maps[i][j] != "X":
                val = 0
                temp = DFS(i,j, val)
                answer.append(temp) 
                
    if answer == []:
        return [-1]
    answer.sort()
    return answer
