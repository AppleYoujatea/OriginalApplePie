import sys
sys.stdin = open("10828.txt", "r")

import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    order = input().split()

    if order[0] == "push":
        stack.append(order[1])

    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif order[0] == "size":
        print(len(stack))

    elif order[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)