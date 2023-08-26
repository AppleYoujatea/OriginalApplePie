def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    cnt = 0
    for k in cities:
        k = k.lower()
        if cacheSize:
            if not k in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                    # 현재 있는 cache의 수와 size가 같으면 pop해준다.
                    # 새로 넣어주기 위해서
                cache.append(k)
                cnt += 5
        # 그리고 k를 넣어주고 넣어주므로 cache miss인 실행시간 5를 더해준다.
            else:   # 만약 k가 이미 cache에 있을 경우
                cache.pop(cache.index(k))
                # cache에서 k의 위치를 찾아 그것을 pop해준다.
                cache.append(k)
                cnt += 1
        # 그리고 새로 k를 cache에 넣어주고, cache hit 이므로 1을 더한다.
        else:
            cnt += 5
        # cachesize가 0일 경우에는 계속 miss일것이므로 5를 더해준다.
        
    # 너무 LRU 알고리즘을 알아야 한다.
    # 그래도 배열에 대하여 append하고 pop하는 데에 익숙해질 수 있었다..
    
    return cnt
