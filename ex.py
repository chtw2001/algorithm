import sys
import math
from collections import defaultdict, deque
from heapq import heappush as push, heappop as pop

a = [1,2]
a[-1:] = [40]
print(a)

a = [1,2]
a[len(a):] = [40]
print(a)
print(1)

a = [1,2]
a[0:] = [40]
a.pop()
print(a)

a = 1
for i in range(1, 11):
    a *=i
print(a)