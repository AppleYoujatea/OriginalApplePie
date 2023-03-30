inputString = input()
inputString2 = input()

LCS = []
i = 0
j = 0
temp = ""
if len(inputString) > len(inputString2):
    temp = inputString
    inputString = inputString2
    inputString2 = temp


while True:
    if i == len(inputString):
        break
    elif j == len(inputString2):
        j = i
        i += 1
    elif inputString[i] == inputString2[j]:
        LCS.append(inputString[i])
        i += 1
        j += 1

    elif inputString[i] != inputString2[j]:
        j += 1
print(len(LCS))



