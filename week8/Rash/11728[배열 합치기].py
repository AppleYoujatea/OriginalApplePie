# 문제
# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

A, B = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

combineList = A_list + B_list
combineList.sort()
for i in range(len(combineList)):
    print(combineList[i], end= " ")
