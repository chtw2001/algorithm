# 1번 멘토와 멘티
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())

ary = defaultdict(list)
for _ in range(N):
    mentor, mentee = map(str, input().split())
    ary[mentor].append(mentee)

for key in ary.keys():
    ary[key].sort(reverse=True)

for key in sorted(ary.keys()):
    for value in ary[key]:
        print(key, value)
