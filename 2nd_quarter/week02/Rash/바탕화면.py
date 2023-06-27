def solution(wallpaper):
    answer = [51, 51, 0, 0]
    lx, ly, rx, ry = 0, 1, 2, 3

    for i, elements in enumerate(wallpaper):
        for j, element in enumerate(elements):
            if element == '#':
                answer[lx] = min(answer[lx], i)
                answer[ly] = min(answer[ly], j)
                answer[rx] = max(answer[rx], i + 1)
                answer[ry] = max(answer[ry], j + 1)

    return answer