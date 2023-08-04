
def solution(n, arr1, arr2):
    answer = []
    
    one = []
    for k in arr1:
        st = str(bin(k)[2:])
        while len(st) != n:
            st = '0' + st
        one.append(st)
    two = []
    for k in arr2:
        st = str(bin(k)[2:])
        while len(st) != n:
            st = '0' + st
        two.append(st)
    
    for i in range(n):
        st = ""
        for j in range(n):
            if one[i][j] == "1" or two[i][j] == "1":
                st += "#"
            else:
                st += " "
        answer.append(st)
    
    return answer
