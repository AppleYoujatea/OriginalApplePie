import sys
sys.stdin = open("17276.txt", "r")

"""
풀이 시간: 18:30 ~
시계: 주 -> 가운데열 -> 부 -> 가운데행 -> 주
반시계: 주 -> 가운데행 -> 부 -> 가운데열 -> 주

주: i == j
가운데행: i == (n + 1) / 2
부: i + j == n + 1
가운데열: j == (n + 1) / 2
"""