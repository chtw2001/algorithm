# from functools import reduce
# import sys, math
# from collections import defaultdict, deque
# from heapq import heappush as push, heappop as pop, heapify

# def cal(a):
#     a[1] = 0

# b = [1,2]
# cal(b)
# print(b)

# 4번

a = set()
a.add(1)
b = set()
b.add(2)
c = set()
c.add(3)
c.add(2)
c = c.union(b)
print(c)