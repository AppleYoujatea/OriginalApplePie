import sys
sys.stdin = open("17413.txt", "r")

"""
시간: 09:40 ~ 10:06
뒤집을 tmp
정답 result
입력값 선형 탐색
3. < 만나면: 
        flag = True
        tmp 뒤집어서 result에 저장 -> result에 < 저장 -> tmp 비움
    > 만나면:
        flag = False
        result에 > 저장

    공백 만나면:
        뒤집어서 저장 -> tmp 비움
    
    flag 켜져 있으면:
        result에 저장
    아니면:
        tmp에 저장
"""

result = ""
flag = False
tmp = ""

for i in input():
    if i == "<":
        flag = True
        result += tmp[::-1]
        tmp = ""
        result += i
        continue

    elif i == ">":
        flag = False
        result += i
        continue

    elif i == " ":
        result += tmp[::-1] + " "
        tmp = ""
        continue
        
    if flag:
        result += i

    else:
        tmp += i

print(result+tmp[::-1])