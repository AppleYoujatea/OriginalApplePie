def solution(numbers):
    answer = [-1] * len(numbers)
    
    st = []
    
    for i in range(len(numbers)):
        while st and numbers[st[-1]] < numbers[i]:
            answer[st.pop()] = numbers[i]
            # answer에 st를 pop한 값 (마지막 값)을 인덱스로 해서 비교하고
            # 작을 경우 넣어준다..
        st.append(i)
    
    
    return answer

# 스택을 사용하여 푼 다는 것을 생각하기 어려운 문제라고 생각한다.

# while 문에서 stack의 마지막 인덱스의 값과 numbers[i]를 비교하여 pop함으로써, 뒤큰수가 없는 인덱스가 남도록 합니다.
# 마지막까지 stack에 남아있는 인덱스들은 뒤큰수가 없는 원소들인데 처음에 -1로 설정을 해주어서 괜찮다.
