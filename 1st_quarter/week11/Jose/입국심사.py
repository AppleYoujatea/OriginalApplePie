import sys

ls = []

N, M = map(int, input().split())
for _ in range(N):
    ls.append(int(sys.stdin.readline()))

start = 1
end = max(ls) * M # 최대 소요 시간
answer = end

while (start <= end):

    mid = (start + end) // 2
    total = 0

    for i in range(N):
        total += mid // ls[i] #  mid 시간에 i 번 심사대에서 심사를 받을 수 있는 인원 -?

    if total >= M:
        end = mid - 1
        answer = min(mid, answer) 
    else:
        start = mid + 1 

print(answer)
