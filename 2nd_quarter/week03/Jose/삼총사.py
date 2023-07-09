# 오 .. 무슨 알고리즘이 있으려나 ???
# 가능한 수를 만들라고 했으니 - 
# 예아 좋다 ! 
 
def solution(number):
    answer = 0
    
    length = len(number)
    
    temp = []
    
    for i in range(length):
        temp.append(number[i])
        
        for j in range(i+1, length):
            temp.append(number[j])
            
            for k in range(j+1, length):
                temp.append(number[k])
                if sum(temp) == 0:
                    answer += 1
                temp.pop()
            temp.pop()
        temp.pop()
    return answer
