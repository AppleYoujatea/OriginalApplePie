from collections import deque
q = deque()

import sys
count = int(sys.stdin.readline())

for _ in range(count):
    Req =  sys.stdin.readline().split()

    if Req[0] == "push":
        q.append(Req[1])
   
    elif Req[0] == "pop":
        if not q:
            print("-1")
        else:
            print(q.popleft())
   
    elif Req[0] == "size":
        print(len(q))
    
    elif Req[0] == "empty":
        if not q:
            print("1")
        else:
            print("0")

    elif Req[0] == "front":
        if not q:
            print("-1")
        else:
            print(q[0])

    elif Req[0] == "back":
        if not q:
            print("-1")
        else:
            print(q[-1])