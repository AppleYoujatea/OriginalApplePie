n, k = map(int, input().split())
stuff = [[0, 0]]
for _ in range(n):
    stuff.append(list(map(int, input().split())))
graph = [[0] * (k + 1) for _ in range(n + 1)]

# 물건의 개수
for i in range(1, n + 1):

    # 테스트할 물건의 무게, 가치
    weight, value = stuff[i][0], stuff[i][1]

    # 가방의 무게가 1 ~ k인 경우 테스트
    for j in range(1, k + 1):

        if j < weight: # 현재 가방의 무게보다, 물건의 무게가 무거운 경우 -> 담을 수 없음
            graph[i][j] = graph[i - 1][j] # 같은 가방 무게, 이전 물건인 경우 최대값 가져옴
        else: # 담을 수 있는 경우
            graph[i][j] = max(graph[i-1][j], value + graph[i-1][j - weight]) # max(위의 케이스, 이전 물건 & 같은 무게 - 현재 무게 + 현재 물건의 가치)
    
# print(max(graph[-1]))
print(graph[n][k])