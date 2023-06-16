#첫쨰 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘쨰 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그길이는 20 이하이다.
# N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지다.

from collections import Counter

n,m = map(int,input().split())
people = []
answer = []

for _ in range(n):
    people.append(input())

for _ in range(m):
    people.append(input())

counter = Counter(people)

for key, value in counter.items():
    if value == 2:
        answer.append(key)

print(len(answer))
answer.sort()

for i in range(len(answer)):
    print(answer[i])
