def solution(answers):
    answer = []
    score = [0, 0, 0]
    a = [1,2,3,4,5] # 5
    b = [2,1,2,3,2,4,2,5] # 8
    c = [3,3,1,1,2,2,4,4,5,5] #10
    
    for i in range(len(answers)):
        if (answers[i] == a[i%5]):
            score[0] += 1
        if (answers[i] == b[i%8]):
            score[1] += 1
        if (answers[i] == c[i%10]):
            score[2] += 1    
    
    mx = max(score)
    
    for idx, i in enumerate(score):
        if i == mx:
            answer.append(idx + 1 )
    
            
    return answer
