# aaaa aaa 코너 케이스 찾느라 헤맸다. 
# 12 줄의 + 1 중요하다. 

flag = False 

while True: 
    try:
        a, b = input().split()
        flag = False
        for i in a:
            if i in b:
                    b = b[b.index(i)+1:]
            else:
                print("No")
                flag = True
                break
        if flag is not True:
            print("Yes")

    except:
        break
    
