# want 의 순서는 섞여도 되니 sort
# 10개씩 묶어서 sort 일치하는지 확인하면 안되나
# 

def solution(want, number, discount):
    answer = 0
    
    want_list = []
    
    for i in range(len(want)):
        for _ in range(number[i]):
            want_list.append(want[i])
    want_list.sort()
    
    for i in range(len(discount) - 10 + 1):
        temp = discount[i: i + 10]
        temp.sort()
        if want_list == temp:
            answer += 1
    
    return answer
