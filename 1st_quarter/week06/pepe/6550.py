import sys
sys.stdin = open("6550.txt", "r")

"""
풀이 시간: 12:35 ~ 12 : 40 ~ 12 : 50

s의 인덱스를 i
t의 인덱스를 j로 두고 

while loop, s를 탐색
i가 먼저 끝나면 flag = True
j가 먼저 끝나면 flag = False
s[i] == t[j]이면
    i += 1
    j += 1
아니면
    j += 1

if flag: Yes
else: No
"""

while True:
    try:
        s, t = input().split()
        i = 0
        j = 0
        length_s = len(s)
        length_t = len(t)
        flag = False

        while True:

            if i >= length_s:           # index 고려해서 > 가 아닌 >=
                flag = True
                break                   # 여기에서 break 안 해줘서 시간 씀
            elif j >= length_t:
                break

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if flag:
            print("Yes")
        else:
            print("No")

    except EOFError:
        break

    
