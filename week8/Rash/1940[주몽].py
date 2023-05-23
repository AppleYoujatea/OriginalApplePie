total = int(input())
weight = int(input())

ingredients = list(map(int, input().split()))

ingredients.sort()
counts = 0
start = 0
end = total - 1
while start < end:
    if ingredients[start] + ingredients[end] == weight:
        counts += 1
        start += 1
        end -= 1
    elif ingredients[start] + ingredients[end] < weight:
        start += 1
    else:
        end -= 1

print(counts)
