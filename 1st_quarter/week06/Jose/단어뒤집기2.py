# 특별히 더 신경 쓴 것은 없었다. 
# count 로 삽입할 순서를 맞춰준 것 조금 헤맸다.


a = input()


inbar = False
result = []
element = []
inbar_element = []
count = 0

for i in a:
    if inbar == False and i == " ":
        result.append("".join(element))
        element = []
        count = 0
    elif i == "<":
        inbar = True
        inbar_element.append(i)
        count = len(element)
    elif i == ">":
        inbar_element.append(i)
        inbar = False
        element.append("".join(inbar_element))
        count += 1
        inbar_element = []
    else:
        if inbar:
            inbar_element.append(i)
        else:            
            element.insert(count, i)
            
    
    
result.append("".join(element))
element = []

for i in result:
    print(i, end = " ")

    
