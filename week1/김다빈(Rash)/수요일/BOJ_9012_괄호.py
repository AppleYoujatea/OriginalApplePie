import sys
count = int(sys.stdin.readline())

for _ in range(count):

     CheckAnswer = input()
     Check_Open = CheckAnswer.count("(")
     Open_Count = 0
     Close_Count = 0
     Flag_Check = 0
     Check_Close = CheckAnswer.count(")")
     for i in range(len(CheckAnswer)):
          if CheckAnswer[i] == "(":
                Open_Count+=1
          elif CheckAnswer[i] == ")":
               Close_Count+=1
          if Open_Count<Close_Count:
                Flag_Check = 1
                break
   
     if len(CheckAnswer)/2 == Check_Open and len(CheckAnswer)/2 == Check_Close and CheckAnswer[0] == "(" and Flag_Check != 1:{
               print("YES")
              
       }
     else:{
               print("NO")
     }