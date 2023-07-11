def solution(number, limit, power):
    count = 0
    arrs = []
    
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** 0.5)+1):
            if i % j == 0:
                count +=2
                if j**2==i: 
                    count-=1
        if count > limit:
            arrs.append(power)
        else:
            arrs.append(count)    

    return sum(arrs)
