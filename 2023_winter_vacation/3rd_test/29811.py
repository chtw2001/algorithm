# 5번
from collections import defaultdict
import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N, M = map(int, input().split())
ary = []
for i in range(2):
    ary += list(map(int, input().split()))

def check(heap):
    if not dict[heap[0][1]]:
        return heap[0][1]
    if dict[heap[0][1]] == heap[0][0]:
        return heap[0][1]
    pop(heap)
    return check(heap)

l_heap = []
r_heap = []
for i in range(N+M):
    if i < N:
        push(l_heap, (ary[i], i+1))
    else:
        push(r_heap, (ary[i], i+1))

K = int(input())
dict = defaultdict(int)
while K:
    order = list(map(str, input().split()))
    if order[0] == 'U':
        way, people = int(order[1]), int(order[2])
        if way <= N:
            push(l_heap, (people, way))
            dict[way] = people              
        else:
            push(r_heap, (people, way))
            dict[way] = people
    else:
       print(check(l_heap), check(r_heap))
    
    K -= 1