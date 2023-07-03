"""
풀이 시간: 16:10 ~

survey 리스트 : [성격 유형 2가지]
4개의 지표 중에, 점수가 높은 것을 선택
점수가 같다면, 사전 순으로 빠른 것을 선택
"""

def solution(survey, choices):
    # 성격 유형별 점수를 저장할 딕셔너리 초기화
    scores = {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }

    # 각 설문 조사의 응답에 따라 해당하는 성격 유형에 점수 추가
    for pers, choice in zip(survey,choices):
        if choice > 4:     
            scores[pers[1]] += choice - 4
        elif choice < 4:   
            scores[pers[0]] += 4 - choice

    # 결과 문자열 초기화
    result = ''

    # 성격 유형별로 점수를 비교하고, 더 높은 점수를 가진 성격 유형을 결과 문자열에 추가
    # 같은 점수라면 사전 순서가 빠른 것을 추가
    pers_types = list(scores.items())

    for i in range(0, len(pers_types), 2):
        if pers_types[i][1] < pers_types[i+1][1]:
            result += pers_types[i+1][0]
        else:
            result += pers_types[i][0]
    
    return result


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))