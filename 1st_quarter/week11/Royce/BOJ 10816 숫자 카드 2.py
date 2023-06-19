


# import sys
# sys.stdin = open('./work.txt', 'r')


from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

ans = []
count = Counter(arr)
# Counter는 리스트를 값으로 넣어주면 해당 원소들이 몇번 등장했는지
# 찾아서 딕셔너리 형태로 반환한다.

# 원래는 이분탐색 문제이므로 이분탐색으로 복잡하게 푸는 방법도 있으나
# C++을 사용하면 upper_bound, lower_bound로도 쉽게 풀 수도 있다...
# 파이썬을 사용해야 하는 이유..?

for i in range(len(arr2)):
    if arr2[i] in count:
        print(count[arr2[i]], end = ' ')
    else:
        print(0, end= ' ')
