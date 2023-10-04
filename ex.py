from collections import deque, defaultdict
from heapq import heappush as push, heappop as pop, heapify
import sys, random, math
from itertools import combinations

# case = 1
# while 1:
#     a, b = map(int, input().split())
#     if a == b == 0:
#         break
#     cnt = i = 0
#     while (i+1)*i // 2 < a:
#         i += 1
#     while (i+1)*i // 2 < b-1:
#         t = (i+1)*i // 2 + 1
#         if t**0.5 == int(t**0.5):
#             cnt += 1
#         i += 1
#     print(f"Case {case}: {cnt}")
#     case += 1
a = 6
b = bin(a)[2:][::-1]
p = [idx for idx, digit in enumerate(b) if digit == '1']
print(p)
