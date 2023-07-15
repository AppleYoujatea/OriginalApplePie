# 풀이계획
# 1. 각각의 수포자가 어떤 정답을 썼는지 리스트화 하기
# 2. 정답 어레이와 각각의 수포자 리스트와 답 비교하기
# 3. 비교한 후 정답이 많은 순서대로 answer에 넣고 동점이면 오름차순으로 정렬해주기
def solution(answers):
    answer = []
    num1 = [0] * len(answers)
    num2 = [0] * len(answers)
    num3 = [0] * len(answers)
    num2_list = [2, 1, 2, 3, 2, 4, 2, 5]
    num3_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num1_answer = 0
    num2_answer = 0
    num3_answer = 0
    tmp = 1
    num2cnt = 0
    num3cnt = 0
    # 1번 수포자가 문제수 만큼 찍는 방식
    for i in range(len(answers)):
        num1[i] = tmp
        tmp += 1
        if tmp == 6:
            tmp = 1
    # 2번 수포자가 문제수 만큼 찍는 방식
    for i in range(len(answers)):
        num2[i] = num2_list[num2cnt]
        num2cnt += 1
        if num2cnt == len(num2_list):
            num2cnt = 0

    # 3번 수포자가 문제 수 만큼 찍는 방식
    for i in range(len(answers)):
        num3[i] = num3_list[num3cnt]
        num3cnt += 1
        if num3cnt == len(num3_list):
            num3cnt = 0

    # 1,2,3번 수포자와 정답을 비교하는 반복문
    for k in range(len(answers)):
        if num1[k] == answers[k]:
            num1_answer += 1
        if num2[k] == answers[k]:
            num2_answer += 1
        if num3[k] == answers[k]:
            num3_answer += 1

    answer_list = [num1_answer, num2_answer, num3_answer]

    for i in range(len(answer_list)):
        if answer_list[i] == max(answer_list):
            answer.append(i + 1)

    return answer
