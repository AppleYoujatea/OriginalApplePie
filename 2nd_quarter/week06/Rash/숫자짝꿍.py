#각 x,y를 딕셔너리화했다
#그리고 공통부분 딕셔너리를 만들었다
#마지막으로 공통부분 딕셔너리를 내림차순 정렬 후 예외조건 처리
def solution(X, Y):
    xdict = {}
    ydict = {}
    samedict = {}
    answer = ''

    for i in X:
        if i in xdict:
            xdict[i] = xdict[i] + 1
        else:
            xdict[i] = 1

    for j in Y:
        if j in ydict:
            ydict[j] = ydict[j] + 1
        else:
            ydict[j] = 1

    for k in range(10):
        if str(k) in xdict and str(k) in ydict:
            if xdict[str(k)] > ydict[str(k)]:
                samedict[str(k)] = ydict[str(k)]
            else:
                samedict[str(k)] = xdict[str(k)]
    a = list(samedict.keys())
    a.sort(reverse=True)

    for p in range(len(a)):
        answer += a[p] * samedict[a[p]]

    if answer == "":
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"

    return answer