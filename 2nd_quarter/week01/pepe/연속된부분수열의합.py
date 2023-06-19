"""
누적합 만듦
누적합을 투포인터로 탐색하며 구간합 구함
구간합이 k와 일치하면 tmp_list에 저장
길이로만 정렬 ?
"""

def solution(sequence, k):

    result = []
    prefix = [0] * (len(sequence) + 1)

    for i in range(len(sequence)):
        prefix[i + 1] = prefix[i] + sequence[i]

    left = 0
    right = 1

    while left < right:

        if right > len(sequence):
            break

        tmp = prefix[right] - prefix[left] # 실제 인덱스 위치 반영

        if tmp == k:
            result.append([left, right-1]) # 실제 인덱스 위치 반영
            right += 1

        elif tmp < k:
            right += 1

        elif tmp > k:
            left += 1

    # 1. 길이가 짧은 순서, 2. 시작 인덱스가 빠른 순서
    answer = sorted(result, key=lambda k: (k[1] - k[0], k[0]))

    return answer[0]

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))