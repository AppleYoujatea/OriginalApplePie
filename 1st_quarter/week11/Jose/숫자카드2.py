N = int(input())
ns = list(map(int, input().split()))

ns_dict = {}

for i in ns:
    if i not in ns_dict:
        ns_dict[i] = 1
    else:
        ns_dict[i] += 1

M = int(input())
ms = list(map(int, input().split()))
counts = [0 for _ in range(M)]

for idx, i in enumerate(ms):
    if i in ns_dict:
        counts[idx] = ns_dict[i]
    else:
        counts[idx] = 0
# 시간초과왜요 ;;

# for idx, m in enumerate(ms):
#     start = 0
#     end = len(ns) - 1
#     while start <= end:
#         mid = (start + end) // 2 # count 시작 전 확인
#         if ns[mid] < m:
#             start = mid + 1
#         else: # mid > m 
#             end = mid - 1 
    
#     check = end 
#     count = 0
#     while(check < len(ns) and ns[check] == m):
#         count += 1
#         check -= 1
#     check = end + 1          
#     while(check < len(ns) and ns[check] == m): # check += 1 
#         count += 1
#         check += 1
#     counts[idx] = count

result = " ".join(map(str, counts)) 
print(result)

