from functools import reduce
import sys, math
from collections import defaultdict, deque
from heapq import heappush as push, heappop as pop

a = [1,2,3,4]
s = map(lambda x:x*x, a)
for z in s:
    print(z)
print()

a = [1,2,3,4]
s = filter(lambda x:x%2, a)
for z in s:
    print(z)
print()

a = [1,2,3,4]
s = reduce(lambda x, y:x+y, a)
print(s)