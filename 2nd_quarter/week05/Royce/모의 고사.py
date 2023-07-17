def solution(answers):
    answer = []
    
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(answers)):
        if answers[i] == arr1[i % len(arr1)]:
            num1+=1
        if answers[i] == arr2[i % len(arr2)]:
            num2+=1
        if answers[i] == arr3[i % len(arr3)]:
            num3+=1
    num = [num1, num2, num3]
    
    for idx, s in enumerate(num):
        if s == max(num):           ## 최대 값과 같을 경우
            answer.append(idx+1)    ## 그 경우의 인덱스를 넣어준다.
    
    return answer
