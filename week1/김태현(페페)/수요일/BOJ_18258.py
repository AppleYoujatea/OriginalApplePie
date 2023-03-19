import sys
sys.stdin = open("18258.txt", "r")

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    order = input().split()

    if order[0] == "push":
        q.append(order[1])
    
    if order[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    
    if order[0] == "size":
        print(len(q))
    
    if order[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    
    if order[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    
    if order[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    
