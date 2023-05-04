import collections

word =input()
check = collections.Counter(word)

cnt = 0
result = ""
mid = ""

for k, v in list(check.items()):
    if v % 2 == 1: 
        cnt += 1
        mid = k
        if cnt >= 2: 
            print("I'm Sorry Hansoo")
            break
else:
    for k, v in sorted(check.items()): 
        result += (k * (v // 2)) 

    print(result + mid + result[::-1])