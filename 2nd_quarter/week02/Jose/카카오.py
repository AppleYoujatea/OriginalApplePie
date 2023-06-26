from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    terms_dict = {}
    for i in terms: 
        typ, mth = i.split()
        terms_dict[typ] = mth
    
    privacies_dict = {}
    for num, j in enumerate(privacies):
        dte, typ = j.split()
        
        year, mth, day = dte.split(".")
        addition = int(terms_dict[typ])
        
        if (int(mth) + addition) > 12:
            # print(int(mth) + int(addition)/12)
            if (int(mth) + addition)%12 == 0:
                year = str(int(year) + int((int(mth) + int(addition))/12) - 1)
                mth = 12
            else: 
                year = str(int(year) + int((int(mth) + int(addition))/12))
                mth = (int(mth) + addition)%12
            
            
            if mth < 10:
                mth = "0" + str(mth)
            else: 
                mth = str(mth)
            
        else:
            mth = int(mth) + addition
            if mth < 10:
                mth = "0" + str(mth)
            else: 
                mth = str(mth)
        
        
        today_date = today.replace(".", "")
        compare_date = year + mth + day
        if (int(today_date) - int(compare_date)) >= 0 : 
            answer.append(num + 1)
        
        
    return answer
