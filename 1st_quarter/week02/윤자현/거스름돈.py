n = int(input())

answer_5 = 0
answer_2 = 0

while(n):
    if n >= 5:
      answer_5 += n // 5 
      n = n % 5
    elif n >= 2:
      answer_2 += n // 2
      n = n % 2
    else:
        if answer_5 != 0:
            n += 5
            answer_5 -= 1 
            answer_2 += n // 2
            n = n % 2
        else:
          print(-1)
          break
          
if n == 0:
  print(answer_5 + answer_2)

	
