"""
풀이 시간: 17:15 ~

1. 해쉬맵 -> 최소값일 때만 갱신하도록
2. 순방향 탐색

1번으로 ㄱㄱ
1. key_dict = {alphabet : dist}
2. keymap을 탐색하며 dist를 최솟값으로 갱신

3. targets을 탐색하며, 길이 구함
4. so easy
"""

from collections import defaultdict

def solution(keymap, targets):
    answer = []
    
    # 키보드를 defaultdict로 만들고, 각 글자를 누르는 데 필요한 횟수를 저장
    key_dict = defaultdict(lambda: float('inf'))  # 아무 키도 누르지 않은 상태를 무한대로 초기화

    for km in keymap:
        for j, alphabet in enumerate(km, start=1):
            key_dict[alphabet] = min(key_dict[alphabet], j)

    for target in targets:
        press_count = 0
        for t in target:
            if t in key_dict:
                press_count += key_dict[t]
            else:
                press_count += float('inf')

        # 문자열을 만드는 데 필요한 키 누름 횟수가 무한대라면 -1을 추가
        if press_count == float('inf'):
            answer.append(-1)
        else:
            answer.append(press_count)
    
    return answer

keymap = ["AA", "AC"]
targets = ["B", "F"]
print(solution(keymap, targets))  # Output: [-1, -1]

