# 3번 중앙값 제거
import sys, math
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

# N = int(input())
# ary = list(map(int, input().split()))

# min_heap, max_heap = [], []

# def push_num(num):
#     push(max_heap, -num)
#     if min_heap and -max_heap[0] > min_heap[0]:
#         push(max_heap, -pop(min_heap))
#         push(min_heap, -pop(max_heap))

# for i in range(N):
#     if i % 2:
#         push(min_heap, ary[i])
#         if -max_heap[0] > min_heap[0]:
#             push(max_heap, -pop(min_heap))
#             push(min_heap, -pop(max_heap))
#     else:
#         push(max_heap, -ary[i])
#         if min_heap and -max_heap[0] > min_heap[0]:
#             push(max_heap, -pop(min_heap))
#             push(min_heap, -pop(max_heap))

# cnt = 0
# while max_heap:
#     cnt += int(math.log2(-pop(max_heap)))

# print(cnt+1)

# ver2
N = int(input())
cnt = 0
ary = sorted(list(map(int, input().split())))

for i in ary[:(N+1)//2]:
    cnt += int(math.log2(i))

print(cnt+1)
