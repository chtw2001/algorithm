import sys
import math
from collections import defaultdict, deque
from heapq import heappush as push, heappop as pop

a = 1
for i in range(1, 11):
    a *=i
print(a)