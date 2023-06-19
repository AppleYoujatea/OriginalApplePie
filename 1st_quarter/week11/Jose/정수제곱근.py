num = int(input())

start = 0
end = num

while start <= end: 
    mid = (start + end) // 2
    if mid ** 2 >= num:
        end = mid - 1
    else: 
        start = mid + 1 
if end ** 2 != num:
    print(end + 1)
else:
    print(end)
