from collections import deque, defaultdict
from heapq import heappush as push, heappop as pop, heapify
import sys, random
from itertools import combinations


a = deque()
for i in range(5):
    a.append(i)
print(a)
for i in range(5):
    print(a[i])
    del a[i]
print(a)