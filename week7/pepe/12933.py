import sys
sys.stdin = open("12933.txt", "r")

"""
풀이 시간: 23:12 ~ 

오리 한 마리가 quack을 반복적으로 외칠 수 있음
입력값을 보고, 최소 오리 개수를 구해야 함
quack과 입력값을 투 포인터로 탐색 (i, j)
입력값을 순회하며 quack을 찾으면 cnt += 1, i = 0
cnt == 0 이면 -1
아니면 개수 출력
"""



s = input()
size = len(s)
visited = [0] * size
quack = 'quack'
cnt = 0

if size % 5 != 0:
    print(-1)
    exit()
    
def duck(start):
    global cnt
    idx = 0
    keep = True
    for i in range(start, size):
        if s[i] == quack[idx] and visited[i] == 0:
            visited[i] = 1
            if quack[idx] == 'k':
                if keep:
                    cnt += 1
                    keep = False
                idx = 0
            else:
                idx += 1

for i in range(size):
    duck(i)

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)