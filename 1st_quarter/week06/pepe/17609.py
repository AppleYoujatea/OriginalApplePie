import sys
sys.stdin = open("17609.txt", "r")

"""
풀이 시간: 13 : 30 ~ 14 : 11 ~

- 투포인터
1. 뒤집어서 새로운 문자열 만듦
2. -> 같으면 회문 0 
3. -> 다르면 왼쪽 제거 or 오른쪽 제거 -> 투포인터 탐색 -> 하나만 같으면 회문 1
4. 이도 저도 아니면 회문 2
"""
import sys

def secondCheck(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def firstCheck(word,left,right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = secondCheck(word,left+1,right)
            check2 = secondCheck(word,left,right-1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0

n = int(input())
for _ in range(n):
    word = input()
    left=0
    right=len(word)-1
    ans = firstCheck(word,left,right)
    print(ans)
