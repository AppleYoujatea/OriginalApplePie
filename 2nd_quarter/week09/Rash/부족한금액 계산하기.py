#풀이계획
#1. totalPrice 변수를 선언
#2. tmpPrice로 계속 올라가는 변수 저장해놓기
#3. totalPrice값을 구해서 Money를 빼면 부족한 금액이 나온다.
#4. 만약 totalPrice 보다 money가 작으면 0을 return해라

def solution(price, money, count):
    totalPrice = 0
    tmpPrice = 0
    for i in range(count):
        tmpPrice += price
        totalPrice += tmpPrice
    if totalPrice < money:
        return 0
    answer = totalPrice - money
    return answer