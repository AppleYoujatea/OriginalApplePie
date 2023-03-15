answer = []

n = int(input())

for _ in range(n): 
  i = str(input())
  answer = []
  yes = True
  for j in i:
    if j == "(":
      answer.append(j)
    else:
      if answer:
        answer.pop()
      else:
        yes = False
        break
  if yes and len(answer) == 0: 
    print("YES")
  else:
    print("NO")
