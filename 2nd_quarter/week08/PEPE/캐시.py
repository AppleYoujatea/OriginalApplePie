"""
풀이 시간: 16:51 ~

LRU 뼈대 코드를 작성한 뒤에,
문제에 맞게 수정해서 제출하자
"""

def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    cache = []
    
    for city in cities:
        city = city.lower() # 소문자로 통일
        if city not in cache: # 현재 캐시에 도시가 없다면? cache miss == 5
            answer += 5
            if len(cache) < cacheSize: # 사이즈 제한보다 작다면? 추가
                cache.append(city)
            else:       # 사이즈 제한을 채웠다면? 가장 마지막에 참조한 값을 제거하고, 추가
                if cache:
                    cache.pop(0)
                cache.append(city)
        else:                 # 현재 캐시에 도시가 있다면? cache hit == 1
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
    
    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))