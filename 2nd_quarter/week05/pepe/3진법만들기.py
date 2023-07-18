def to_ternary(n):
    result = []
    while n > 0:
        result.append(str(n % 3))
        n //= 3
    return "".join(result[::-1])

def to_decimal(n: str):
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * (3 ** (len(n) - 1 - i))
    return decimal

def solution(n):
    ternary = to_ternary(n)
    flipped_ternary = ternary[::-1]
    answer = to_decimal(flipped_ternary)
    return answer

n = 45
print(solution(n))
