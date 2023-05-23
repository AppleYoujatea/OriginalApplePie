# 문제
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.


A, B = map(int, input().split())

N = list(map(int, input().split()))

count = 0
start = 0
end = 0
while end <= len(N):
    if sum(N[start:end]) < B:
        end += 1
    elif sum(N[start:end]) > B:
        start += 1
    elif sum(N[start:end]) == B:
        count += 1
        end += 1

print(count)


