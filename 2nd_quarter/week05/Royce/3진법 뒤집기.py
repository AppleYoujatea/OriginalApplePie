def solution(n):
    answer = 0

    st = ""
    while n != 0:
        st += str(n % 3)
        n //= 3
    
    answer = int(st, 3)
    

    return answer
