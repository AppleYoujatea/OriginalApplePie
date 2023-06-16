//원래 풀었던 버전 ! 디버깅 못함 

txt = str(input())
duck = 0
finish = False

record = [0,0,0,0,0]
flag = True

for i in txt:
    # print(i + "is ongoing")
    # print(record)
    if i == "q":
        if finish is not True:
            finish = False
            duck += 1
        record[0] += 1
    elif i == "u":
        if record[0] > record[1]:
            record[1] += 1
        else:
            print("-1")
            flag = False
            break
    elif i == "a":
        if record[1] > record[2]:
            record[2] += 1
        else:
            print("-1")
            flag = False
            break
    elif i == "c":
        if record[2] > record[3]:
            record[3] += 1

        else:
            print("-1")
            flag = False
            break
    elif i == "k":
        if record[3] > record[4]:
            record[4] += 1
            finish = True
        else:
            print("-1")
            flag = False
            break
    else: 
        print("-1")
        flag = False
        break


if flag:
    if record[0] == record [1] == record[2] == record[3] == record[4] != 0:
        print(duck)
    else:
        print("-1")



// 답지 보고 배웁니다 ㅠㅠ
inp = list(input()) 
quack = ['q','u','a','c','k']
len_inp = len(inp) 
idx = 0 
answer = 0 
visited = [False] * len_inp 
first = False

if len_inp % 5 != 0 or inp[0] != "q": 
    print(-1) 
    exit() 
    
for a in range(len_inp): 
    if inp[a] == "q" and not visited[a]: 
        first = True 
        for i in range(len_inp): 
            if not visited[i] and quack[idx] == inp[i]: 
                visited[i] = True 
                if inp[i] == "k": 
                    if first: 
                        answer += 1 
                        first = False 
                    idx = 0 
                    continue 
                idx += 1 
if answer == 0 or not all(visited): 
    print(-1) 
else: 
    print(answer)
