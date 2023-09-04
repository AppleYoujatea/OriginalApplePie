# sort(reverse = True)
# pop() -> O(1) 
# pop(0) -> O(N)

# 빼주는 것들(-, pop) 전부 while 에서 확인해줘야 런타임 에러 안남

def solution(d, budget):
    answer = 0
    d.sort(reverse = True)
    while budget and d: 
        regist = d.pop()
        if budget >= regist:
            budget -= regist 
            answer += 1 
        else: 
            break
    return answer
