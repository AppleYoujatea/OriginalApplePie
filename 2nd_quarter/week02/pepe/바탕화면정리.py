"""
풀이 시간: 15: 44 ~

모든 "#"의 인덱스를 탐색
[min_x, min_y, max_x + 1, max_y + 1]

1. wallpaper를 2중 for문으로 탐색하며, min_x, min_y, max_x, max_y를 찾음
2. 최종 값을 [min_x, min_y], [max_x + 1, max_y + 1] 형태로 출력
"""

def solution(wallpaper):

    x_idx_list = []
    y_idx_list = []

    for i in range(len(wallpaper)): # 세로 길이, x
        for j in range(len(wallpaper[0])): # 가로 길이, y
            
            # 파일("#")을 발견하면, index를 저장
            if wallpaper[i][j] == "#":
                x_idx_list.append(i)
                y_idx_list.append(j)

    return [min(x_idx_list), min(y_idx_list), max(x_idx_list) + 1, max(y_idx_list) + 1]

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	
print(solution(wallpaper))