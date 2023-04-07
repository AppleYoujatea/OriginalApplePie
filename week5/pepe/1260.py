import sys
sys.stdin = open("1260.txt", "r")

"""
인접 그래프
방문처리 그래프 0 -> 1 (dfs) -> 0 (bfs) -> 출력

노드 + 1 크기의 그래프 생성
간선 크기만큼 반복
    인접 그래프 input

dfs 함수
시작 노드를 v로
기준 노드의 인접 노드 방문 -> 인접 노드1의 인접 노드 방문 -> ... -> dfs
방문 처리할 때마다 노드 번호 print

bfs 함수
시작 노드를 v로
기준 노드의 모든 인접 노드를 큐에 넣음 -> 인접 노드1의 모든 인접 노드 큐에 넣음 -> ... -> bfs
방문 처리할 때마다 노드 번호 print
"""

from collections import deque

n, m, v = map(int, input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    graph[v].sort()
    visited[v] = 1
    print(v, end=" ")

    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0

    while q:
        x = q.popleft()
        print(x, end=" ")

        for node in graph[x]:
            if visited[node] == 1:
                visited[node] = 0
                q.append(node)

print(graph)

dfs(v)
print()
bfs(v)