inputx = int(input())
Change = [500,100,50,10,5,1]
origin =  1000
numcount = 0
aftercount = 0
origin = origin - inputx
for i in range(len(Change)):
    a = origin//Change[i]
    numcount = numcount + a
    origin= origin%Change[i]

    
print(numcount)

