def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for j in range(int(food[i]/2)):
            answer += str(i)
            
    answer_rev = answer[::-1]
    answer = str(answer) + "0" + str(answer_rev)
                                                   
    return answer


# 7 -> 7 / 2 = 3.5 -> 3 
# range(3) -> 0, 1, 2, 

# 8 -> 8 / 2 = 4
# range(4) -> 0, 1, 2, 3, 4 good ! 
