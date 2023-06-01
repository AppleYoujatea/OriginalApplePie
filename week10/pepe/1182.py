import sys
sys.stdin = open("1182.txt", "r")

"""
풀이 시간: 11:30 ~

n, s 입력 받음
nums 배열 입력 받음
빈 베열 ans 생성
check() 함수 호출
ans 합을 확인해서 s와 일치하면 cnt += 1
nums를 반복하며, ans에 없으면 추가, check()를 재귀적으로 호출, 추가한 원소를 pop
cnt 출력

--> 시간 초과

"""

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ansVal = 0
ansArr = []
cnt = 0

def check():
    global cnt
    global ansVal
    
    if ansVal == s:
        cnt += 1
        return
    
    for num in nums:
        if num not in ansArr:
            ansArr.append(num)
            ansVal += num
            check()
            ansVal -= num
            ansArr.pop()

check()
print(cnt)