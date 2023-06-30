"""
풀이 시간: 16:10 ~

survey 리스트 : [성격 유형 2가지]
4개의 지표 중에, 점수가 높은 것을 선택
점수가 같다면, 사전 순으로 빠른 것을 선택
"""

def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())

    for i in range(0, len(li), 2):
        if li[i][1] < li[i+1][1]:
            answer += li[i+1][0]
        else:
            answer += li[i][0]
    
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))