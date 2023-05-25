# KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
#
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
#
# 예를 들어, 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액의 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
#
# 산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

a = int(input())

A_list = list(map(int, input().split()))
answer_list = [A_list[0], A_list[-1]]
A_list.sort()
end = len(A_list) - 1
start = 0

target = abs(A_list[0] + A_list[-1])
while start < end:

    if target * 1 >= A_list[start] + A_list[end] >= target * -1:
        target = abs(A_list[start] + A_list[end])
        answer_list[0] = A_list[start]
        answer_list[-1] = A_list[end]

    if A_list[start] + A_list[end] >= 0:
        end -= 1
    elif A_list[start] + A_list[end] < 0:
        start += 1

    if target == 0:
        break

for i in range(len(answer_list)):
    print(answer_list[i], end=" ")
