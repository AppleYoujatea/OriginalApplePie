def solution(name, yearning, photo):
    answer = []
    
    arr = dict()
    
    for i in range(len(name)):
        arr[name[i]] = yearning[i]
    
    for i in range(0,len(photo)):
        num = 0
        for j in range(0,len(photo[i])):
            if photo[i][j] in arr.keys():
                photo[i][j] = arr[photo[i][j]]
            else:
                photo[i][j] = 0
            # 없을때는 0을 넣는 것도 고려해 주어야 한다.
            
    for i in photo:
        answer.append(sum(i))
        #     cnt = arr[photo[i][j]]
        #     num += cnt
        # answer.append(num)
    
    return answer
