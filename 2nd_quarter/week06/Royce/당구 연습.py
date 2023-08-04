def solution(m, n, startX, startY, balls):
    answer = []
    
    
    for arr in balls:
        difx = startX - arr[0]
        dify = startY - arr[1]
        
        up = (difx ** 2) + ((n - startY) + (n - arr[1])) ** 2
        down = (difx ** 2) + (startY + arr[1]) ** 2
        
        left = (startX + arr[0]) ** 2 + (dify ** 2)
        right = ((m - startX) + (m - arr[0])) ** 2 + (dify ** 2)
        
        if difx == 0:
            if dify > 0:
                ans = min(left, right, up)
            else:
                ans = min(left, right, down)
                
        elif dify == 0:
            if difx > 0:
                ans = min(up, down, right)
            else:
                ans = min(up, down, left)
        else:
            ans = min(up, down, left, right)
    
        answer.append(ans)
    
    
    return answer
