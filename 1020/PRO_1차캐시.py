from collections import deque

def solution(cacheSize, cities):
    ans = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:  # 캐시 안에 이미 있을 경우
            cache.remove(city)
            cache.append(city)
            ans += 1
        else:  # 캐시 안에 없을 경우
            cache.append(city)
            ans += 5
    return ans