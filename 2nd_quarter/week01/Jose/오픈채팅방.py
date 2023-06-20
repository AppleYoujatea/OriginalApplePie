def solution(record):
    answer = []
    
    records_split = []
    final_name = {}
    
    for i in record:
        temp = i.split() 
        if temp[0] == "Enter":
            final_name[temp[1]] = temp[2]
        elif temp[0] == "Change":
            final_name[temp[1]] = temp[2]
    
    for i in record:
        temp = i.split() 
        result = ""
        if temp[0] == "Enter":
            result += final_name[temp[1]]
            result += "님이 들어왔습니다."
        elif temp[0] == "Leave":
            result += final_name[temp[1]]
            result += "님이 나갔습니다."
        else:
            continue
        answer.append(result)
    
    return answer
