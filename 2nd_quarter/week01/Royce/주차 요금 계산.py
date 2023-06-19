import math
def cal(m, fees):
    return fees[1] + math.ceil(max(0, (m - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    answer = []
    
    park = dict()
    arr = dict()
    
    for k in records:
        time, car, status = k.split()
        h, m = time.split(":")
        m = int(h) * 60 + int(m)
        
        if status == "IN":
            park[car] = m
        elif status == "OUT":
            try:
                arr[car] += m - park[car]
            except:
                arr[car] = m - park[car]
            del park[car]
    
    # items는 (key, value)를 뜻하고, key, value는 따로 해준다.
    # 남은 것들에 대하여 최대 요금으로 때리기
    for car, m in park.items():
        try:
            arr[car] += 23*60+59 - m
        except:
            arr[car] = 23*60+59 - m
            
    return [cal(time, fees) for car, time in sorted(list(arr.items()), key = lambda x : x[0])]
# time에 대해서 정렬해서 fee를 넣어줌
    

# 시도했다가 아예 틀림..
# def solution(fees, records):
#     answer = []
    
#     # 기본 시간, 기본 요금, 단위 시간, 단위 요금
#     def cal(n):
#         if n <= fees[0]:
#             return fees[1]
#         else:
#             return (((n - fees[0]) // fees[2]) + 1) * fees[3]
    
#     arr = {}
#     for k in records:
#         come = int(k[:2]) * 60 + int(k[3:5])
#         arr[k[6:10]] = come
    
#     return answer

