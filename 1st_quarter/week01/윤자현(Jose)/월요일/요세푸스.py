n, k = map(int, input().split())
counter = 0

arr = []

for i in range(n):
  arr.append(i+1)

answer_print = "<"

while arr: 
    if counter + k > len(arr): 
        counter = (counter + k - 1 - len(arr))%len(arr)
    else: 
        counter += k - 1
    answer_print += str(arr[counter])
    answer_print += ", "
    arr.pop(counter)

print(answer_print[:-2]+">")

