def solution(dartResult):
    answer = 0
    
    arr = []
    num = ''
    for k in dartResult:
        if k >= '0' and k <= '9':
            num += k
        elif k == "S":
            num = int(num) ** 1
            arr.append(num)
            num = ""
        elif k == "D":
            num = int(num) ** 2
            arr.append(num)
            num = ""
        elif k == "T":
            num = int(num) ** 3
            arr.append(num)
            num = ""
        elif k == "*":
            if len(arr) > 1:    ## 최근 두개에 2배
                arr[-2] = arr[-2] * 2
                arr[-1] = arr[-1] * 2
            else:               ## arr가 그보다 더 작을 경우 지금거에만 2배
                arr[-1] = arr[-1] * 2
        elif k == '#':
            arr[-1] = arr[-1] * -1
            
    
    return sum(arr)
