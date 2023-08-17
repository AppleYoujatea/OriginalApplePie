# 귀찮은 문제다 한글 읽기 귀찮다 
# 이건 그냥 번역 아닌가! 

def convert(bonus):
    if bonus == "S":
        return 1
    elif bonus == "D":
        return 2
    else:
        return 3

def solution(dartResult):
    
    table = []
    num = ""
    answer = []
    
    for i in dartResult:
        if i.isnumeric():
            if len(table) == 0:
                num += i
            else:
                # no option
                temp = int(table[0]) ** table[1]
                answer.append(temp) 
                table = []
                num = i
                
        elif i == "S" or i == "D" or i == "T": 
            table.append(num)
            table.append(convert(i))
            num = ""
        else: 
            temp = int(table[0]) ** table[1]
            if i == "#":
                temp = -temp
            else:
                temp *= 2
                if len(answer) > 0: 
                    answer[len(answer)-1] *= 2
            answer.append(temp)
            table = []
    if len(table) > 0: 
        temp = int(table[0]) ** table[1]
        answer.append(temp) 
        table = []

    return sum(answer)
