Length,middle = map(int, input().split())
CheckArray = []
AnswerArray = []
arrayint = 1
ArrayCount = middle - 1

for arrayint in range(1, Length+1):
    CheckArray.append(arrayint)
AnswerArray.append(middle)

for _ in range(Length - 1):
    for i in range(len(AnswerArray)):
        if AnswerArray[i] == CheckArray[ArrayCount]:
            del CheckArray[ArrayCount]
            ArrayCount -= 1
  
    if( ArrayCount + middle > len(CheckArray) - 1):
        ArrayCount = (ArrayCount + middle) % len(CheckArray)
        AnswerArray.append(CheckArray[ArrayCount]) 
    else:
        ArrayCount += middle
        AnswerArray.append(CheckArray[ArrayCount])

print("<" ,end ="")
for i in range(len(AnswerArray) -1):
    print(AnswerArray[i], end=', ')
print(AnswerArray[-1],end="")
print(">")

