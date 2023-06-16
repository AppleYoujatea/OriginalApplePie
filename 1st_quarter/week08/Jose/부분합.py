n, s = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0
res = 0
length = n

while end < n: 
    # print(start, end, res)
    res = sum(arr[start:end+1])

    if res == s:
        length = min(length, end - start + 1)
        start += 1
    elif res < s:
        end += 1
    else:
        start += 1 
    
print(length)
