import sys
sys.stdin = open("BOJ_9012.txt", "r")

# t = int(input())

# for _ in range(t):
#     data = input()

#     while "()" in data:
#         data = data.replace("()", "")
    
#     if not data:
#         print("YES")
#     else:
#         print("NO")

t = int(input())

for _ in range(t):
    data = input()

    stack = []
    for d in data:
        if d == "(":
            stack.append("(")
        else:
            if not stack:
                stack.append(")")
                break
            elif stack[-1] == "(":
                stack.pop()
    
    if not stack:
        print("YES")
    else:
        print("NO")