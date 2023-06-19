
# 이제 파이썬으로 풀거 같아요
# dictionary를 사용해서 아이디에 대해서 문자열 값을 지정해주는 게 포인트
# Change면 바꾸어 주는데, Enter의 경우는 들어왔다고 표시해주어야 하므로 for문을 두가지 사용하여야 한다.

def solution(record):
    answer = []
    
    arr = dict()
    num = 0
    
    for k in record:
        k = k.split(" ")
        if k[0] == "Enter":
            arr[k[1]] = k[2]
        elif k[0] == "Change":
            arr[k[1]] = k[2]
    # Enter나 Change의 경우 arr의 값을 바꾸어 준다.
            
    for k in record:
        k = k.split(" ")
        st = ""
        if k[0] == "Enter":
            st += arr[k[1]]
            st += "님이 들어왔습니다."
            answer.append(st)
        elif k[0] == "Leave":
            st += arr[k[1]]
            st += "님이 나갔습니다."
            answer.append(st)
    
    
    
    return answer
