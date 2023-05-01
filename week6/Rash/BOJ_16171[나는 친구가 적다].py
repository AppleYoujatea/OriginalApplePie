# 파이썬 문법을 햇갈리지 말자 근데 이거 스위프트로 풀려했는데.. 시간이슈
import  re
S = input()
K = input()

New_S = re.sub(r"[0-9]", "", S)

if K in New_S:
    print(1)
else:
    print(0)