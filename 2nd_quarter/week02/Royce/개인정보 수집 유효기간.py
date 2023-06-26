def solution(today, terms, privacies):
    answer = []
    
    year, month, day = map(int, today.split('.'))
    
    dic = {}
    for k in terms:
        a, b = k.split()
        dic[a] = int(b)
        
    for i in range(len(privacies)):
        date, name = privacies[i].split(' ')
        date_year, date_month, date_day = map(int, date.split('.'))
        
        date_month += dic[name]
        while date_month > 12:
            date_month -= 12
            date_year += 1
            
        if date_year > year:
            continue
        elif date_year == year:
            if date_month > month:
                continue
            elif date_month == month:
                if date_day > day:
                    continue
                    
        answer.append(i+1)
            
    
    
    return answer
