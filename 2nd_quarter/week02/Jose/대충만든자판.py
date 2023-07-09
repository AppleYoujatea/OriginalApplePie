def solution(key, tar):
    answer = []
    dic = {}

    # seperate each char in key, find out the minimum button number
    for i in key:                           
        tmp = list(set(list(i)))       
        for j in tmp:                       
            if(j in dic):                   
                dic[j] = min(dic[j], i.index(j) + 1)
            else:                           
                dic[j] = i.index(j) + 1
                

                
    for i in tar:                           
        tmp = 0                             
        for j in i:                         
            if(j in dic):
                tmp += dic[j]
            else:                           
                tmp = -1                    
                break                 
        answer.append(tmp)              

    return answer
