def solution(sequence, k):
    answer = []
    
    right = 0
    num = 0
    
    for left in range(len(sequence)):
        while right < len(sequence) and num < k:
            num += sequence[right]
            right += 1
            
        if num == k:
            if not answer:
                answer = [left, right-1]
            else:
                if answer[1] - answer[0] > right-1 - left:
                    answer = [left, right-1]
                # else:
                #     answer = answer
                    
        num -= sequence[left]
                    
    
    
    return answer
