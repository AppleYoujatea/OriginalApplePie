#나는 바보다 문제를 제대로 읽지 않아서 하나의 테스트케이스만 입력받는줄 알고 한참 해맸다.. 조건 없는 무한 반복문을 쓸때는 try catch를 써야하는 것 또한 배웠다.
while True:
    try:
        inputString, inputString2 = str(input()).split()
        AL = []
        i = 0
        j = 0
        tmp = 0

        while True:
            if i == len(inputString):
                break
            elif j == len(inputString2):
                j = tmp + 1
                i += 1
            elif inputString[i] == inputString2[j]:
                AL.append(inputString[i])
                tmp = j
                i += 1
                j += 1

            elif inputString[i] != inputString2[j]:
                j += 1
        answer =''.join(AL)
        if answer == inputString:
            print("Yes")
        else:
            print("No")
    except:
        break
