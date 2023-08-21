def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        
        
        num = bin(arr1[i] | arr2[i])
        num = num[2:].zfill(n)
        # 빈 곳 0으로 채우기
        
        num = num.replace('1', '#')
        num = num.replace('0', ' ')
        
        answer.append(num)
        
        
    
    
    
    return answer
