from itertools import product

def solution(users, emoticons):
    answer = [-1, -1]
    
    # 1. 이모티콘 플러스 서비스 가입자 최대로
    # 2. 이모티콘 판매액을 최대로
    # 할인률은 10,20,30,40 중 하나로 된다.. 이걸 못 봤다. 풀때
    
    # product를 사용하면 중복 순열을 구현할 수 있다.
    for discount in product([10, 20, 30, 40], repeat=len(emoticons)):
        new = 0
        cost = 0
        
        for k in users:
            buy_cost = 0
            for i in range(len(discount)):
                if discount[i] >= k[0]:     # 할인율이 discount보다 더 클 경우에
                    buy_cost += (emoticons[i] * (1 - discount[i] / 100))
                    # 그에 관한 buy_cost를 계산해준다.
            if buy_cost >= k[1]: # buy_cost가 가격을 넘을 경우에는 이모티콘을 구매해야하므로
                new += 1
                buy_cost = 0
            # new를 한명 증가시켜주고 플러스를 사면 가격은 다시 돌아가므로
            # buy_cost를 다시 0으로 돌려준다.
            cost += buy_cost
            # 이렇게 계산한 buy_cost를 cost에 더해준다.
        
        # new가 더 클 경우가 우선 순위 이므로 if로 먼저 처리한다.
        if answer[0] < new:
            answer[0] = new
            answer[1] = cost
        elif answer[0] == new:
            answer[1] = max(answer[1], cost)
        # 같은 경우에는 max를 비교하여 더 큰 값을 넣어준다.
    
    return answer
