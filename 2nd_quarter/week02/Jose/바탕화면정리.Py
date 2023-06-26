def solution(wallpaper):
    a = [50, 50, 0, 0]
    
    for yi, y in enumerate(wallpaper):
        for xi, x in enumerate(y):
            if x == "#":
                a = [
                    min(a[0], yi), min(a[1], xi),
                    max(a[2], yi+1), max(a[3], xi+1)
                ]
    return a

