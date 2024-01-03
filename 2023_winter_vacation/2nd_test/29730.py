# 3번
import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N = int(input())
baekjoon = []
other = []
while N > 0:
    ex = input().strip()
    if '/' in ex:
        ex = ex.split('/')
        push(baekjoon, int(ex[1]))
        
    else:
        push(other, (len(ex), ex))
    
    N -= 1

while other:
    print(pop(other)[1])

while baekjoon:
    print(f'boj.kr/{pop(baekjoon)}')