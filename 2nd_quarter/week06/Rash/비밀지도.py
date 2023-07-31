# 풀이 계획
# 주어진 리스트들을 2차원 배열로 이전법화 시킨다.
# 똑같은 크기의 리스트를 만들고 값을 0으로 초기화한다.
# 반복문으로 arr1 혹은 arr2 둘중 하나라도 값이 1이면 똑같의  크기의 리스트에서 #을 추가하고 아니면 " "을 추가한다.

def changebinary(num):
    binary = ""
    while num != 0:
        if num % 2 == 0:
            binary = "0" + binary
            num = num // 2
        else:
            binary = "1" + binary
            num = num // 2

    return binary


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append("")

    for i in range(n):
        arr1[i] = changebinary(arr1[i])
        while len(arr1[i]) != n:
            arr1[i] = "0" + arr1[i]

        arr2[i] = changebinary(arr2[i])
        while len(arr2[i]) != n:
            arr2[i] = "0" + arr2[i]

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                answer[i] = answer[i] + "#"
            else:
                answer[i] = answer[i] + " "
    return answer