import sys
sys.stdin = open("9251.txt", "r")

"""
i == j이면 [i - 1][j - 1] + 1
i != j이면 max([i - 1][j], [i][j - 1])
"""

word1 = input()
word2 = input()
w1, w2 = len(word1), len(word2)
graph = [[0] * (w2 + 1) for _ in range(w1 + 1)]

for i in range(1, w1 + 1):
    for j in range(1, w2 + 1):
        if word1[i - 1] == word2[j - 1]:
            graph[i][j] = graph[i - 1][j - 1] + 1
        else:
            graph[i][j] = max(graph[i][j - 1], graph[i - 1][j])

print(graph[-1][-1])


word1 = input()  # 첫 번째 문자열을 입력받음
word2 = input()  # 두 번째 문자열을 입력받음
w1, w2 = len(word1), len(word2)  # 두 문자열의 길이를 계산하여 변수 w1, w2에 저장함
graph = [[0] * (w2 + 1) for _ in range(w1 + 1)]  # 0으로 초기화된 2차원 리스트를 생성함

for i in range(1, w1 + 1):  # i를 1부터 w1까지 반복
    for j in range(1, w2 + 1):  # j를 1부터 w2까지 반복
        if word1[i - 1] == word2[j - 1]:  # 만약 word1[i-1]과 word2[j-1]이 같으면 -> 현재 비교 중인 문자
            graph[i][j] = graph[i - 1][j - 1] + 1  # graph[i][j]를 graph[i-1][j-1]+1로 갱신함 -> 이전 값 + 1을 현재 위치에
        else:  # 그렇지 않으면
            graph[i][j] = max(graph[i][j - 1], graph[i - 1][j])  # graph[i][j]를 graph[i][j-1]과 graph[i-1][j] 중 큰 값으로 갱신함

print(graph[-1][-1])  # graph의 마지막 요소를 출력함 (두 문자열의 최장 공통 부분 수열의 길이)
