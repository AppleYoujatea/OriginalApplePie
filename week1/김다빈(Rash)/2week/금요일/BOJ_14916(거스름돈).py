inputx = int(input())
Change = [5,2]
CoinCount = 0
numcount = 0
aftercount = 0

while (True):
   if(inputx % Change[0] == 0 ):
        inputx = inputx//Change[0]
        CoinCount = CoinCount + inputx
        inputx = 0
   elif(inputx - Change[0])%2 == 1 and inputx - Change[0] < Change[0] and inputx % Change[1] == 0:
        inputx = inputx//Change[1]
        CoinCount = CoinCount + inputx
        inputx =0
   if(inputx > Change[0]):
       inputx -= Change[0]
       CoinCount +=1
   if(inputx % Change[0] == 0 ):
        inputx = inputx//Change[0]
        CoinCount = CoinCount + inputx
        inputx = 0
   elif((inputx - Change[0])%2 == 1 and inputx - Change[0] < Change[0] and inputx % Change[1] == 0):
        inputx = inputx//Change[1]
        CoinCount =CoinCount + inputx
        inputx = 0
   if(inputx > Change[1]):
       inputx -= Change[1]
       CoinCount +=1
   if(inputx == 1 or inputx == 0):
       break
   
if  inputx == 1 :    
    print(-1)
else:
    print(CoinCount)

