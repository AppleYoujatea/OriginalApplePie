n = int(input())
k = list(map(int, input().split()))
prefix_sum = [k[0]]
answer = 0
## 맨처음에 봤을때 어떻게 접근해할지 생각이 도저히 안나서 답을봤다 이건 수치다.
for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + k[i])
# 배열에 시그마 값들이 저장된다.
for i in range(n):
    answer += k[i] * (prefix_sum[n - 1] - prefix_sum[i])
# x1(x2+x3+x4) + x2(x3+x4) + x3(x4) + x4 의 형태로 바꾼다.
print(answer)
