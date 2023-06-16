# import sys
# input = sys.stdin.readline()
sys.stdin = open("10828.txt", "r")

import sys
a = int(sys.stdin.readline())

stack = []
# a = int(input())

for _ in range(a):
    k = sys.stdin.readline().split()
    b = k[0]
    
    if "push" in b:
        r2 = k[1]
        stack.append(r2)
    elif "top" == b:
        if not stack:
            print("-1")
        else:
            print(stack[-1])
    elif "size" == b:
        print(len(stack))
    elif "pop" == b:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif "empty" == b:
        if not stack:
            print("1")
        elif stack :
            print("0")