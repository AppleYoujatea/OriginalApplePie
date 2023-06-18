"""
풀이 시간: 10:27 ~

name: 이름
yearning: 점수
photo: 각 문제가 2차원 배열로

score = {name : yearning} 형태로 만들고
photos는 score로 점수 측정하면 될 듯? 
"""

from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    # KeyError를 피하기 위해 defaultdict
    # defaultdict로 선언하면, KeyError가 발생했을 때 타입에 따른 초기값을 설정해줌
    # int 초기값의 경우 == 0
    score = defaultdict(int)
    
    # {name : yearning} 형태로 초기화
    for i in range(len(name)):
        score[name[i]] = yearning[i]

    # photo 2차원 배열을 탐색하며, 점수 더해줌
    for pho in photo:
        tmp = 0
        for i in range(len(pho)):
            tmp += score[pho[i]]
        
        answer.append(tmp)

    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))