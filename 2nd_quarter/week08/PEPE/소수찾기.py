"""
풀이 시간: 16:32 ~

1부터 n까지 소수의 개수를 반환하는 함수
일단 드는 생각:
    에라토스테네스의 체
    소수의 판정 여부는 n의 제곱근까지만

에라토스테네스의 체를 공부하고, 적용하자 !
"""



def solution(n):

    # 0, 1은 빼고 2부터 n까지 소수 판별
    arr = [0, 0] + [1 for _ in range(n - 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1: # 현재 수가 소수라면
            j = 2
            # i의 배수는 모두 소수X 처리
            # 마지막 수까지 처리하기 위해서 같거나 작음
            while i * j <= n: 
                arr[i * j] = 0
                j += 1

    return sum(arr)

n = 10
print(solution(n))