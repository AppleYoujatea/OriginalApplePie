def solution(n, arr1, arr2):
    last_answer = []
    answer = [[" " for _ in range(n)] for _ in range(n)]
    for idex, i in enumerate(arr1):
        temp = bin(i)[2:]
        if len(temp) < n:
            for _ in range(n - len(temp)):
                temp = "0" + temp
        
        for jdex, j in enumerate(temp):
            if j == "1": 
                answer[idex][jdex] = "#"
                
    for idex, i in enumerate(arr2):
        temp = bin(i)[2:]
        if len(temp) < n:
            for _ in range(n - len(temp)):
                temp = "0" + temp
                
        for jdex, j in enumerate(temp):
            if j == "1": 
                answer[idex][jdex] = "#"
        
        
    for an in answer:
        last_answer.append("".join(an))
    
    return last_answer
