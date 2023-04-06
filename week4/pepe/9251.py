word1 = input()
word2 = input()
size = max(len(word1), len(word2))
cache = [0] * size

for i in range(len(word1)):
    cnt = 0
    for j in range(len(word2)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1

print(max(cache))