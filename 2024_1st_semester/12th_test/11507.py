# 1번 카드셋트
import sys
from collections import defaultdict
input = sys.stdin.readline

S = list(input().rstrip())
deque = defaultdict(int)
pocket = set()

for i in range(0, len(S), 3):
    card = S[i]+S[i+1]+S[i+2]
    if card in pocket:
        print("GRESKA")
        quit()
    pocket.add(card)
    deque[S[i]] += 1

for i in ["P", "K", "H", "T"]:
    if not deque[i]:
        print(13, end=' ')
        continue
    print(13 - deque[i], end=' ')