import sys
sys.stdin = open("10816.txt", "r")

"""
풀이 시간: 12:58 ~

- Counter로 풀면 쉬울 듯
- 이분 탐색은 어떻게 ?
"""

from collections import defaultdict

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

cnt_dic = defaultdict(int)

# n의 리스트 원소의 개수를 세서, dict 형태로 저장
for n_elem in n_list:
    cnt_dic[n_elem] += 1

# m의 리스트 원소를 탐색하며, dict에 대응하는 값 출력
for m_elem in m_list:
    print(cnt_dic[m_elem], end=" ")