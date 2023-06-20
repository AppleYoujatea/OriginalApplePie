def solution(sequence, k):
    answer = []
    
    temp = []
    for i in range(len(sequence)):
        temp = []
        temp.append(i)
        total = sequence[i]
        if total > k:
            break
        elif total == k:
            answer.append([i,i])
        for j in range(i+1, len(sequence)):
            if total > k:
                break
            elif total == k:
                temp.append(j-1)
                answer.append(temp)
                break
            else:
                total += sequence[j]
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]

