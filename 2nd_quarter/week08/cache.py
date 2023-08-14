def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in cities:
        city = c.lower()
        if city in cache:
            # 이 부분 고려 못함! 새로 들어오면 새롭게 접근한 도시임
            cache.remove(city)
            cache.append(city)
            answer += 1 
        else: 
            if len(cache) < cacheSize:
                cache.append(city)
            else: 
                if cacheSize != 0:
                    cache.pop(0)
                    cache.append(city)
            answer += 5
    return answer
