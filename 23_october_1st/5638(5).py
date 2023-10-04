import sys
from heapq import heappush as push, heappop as pop
input = sys.stdin.readline

N = int(input())
damn = [list(map(int, input().split())) for _ in range(N)]

def bit(num):
    binary = bin(num)[2:][::-1]
    p = [idx for idx, digit in enumerate(binary) if digit == '1']
    return p


TC = int(input())
for tc in range(1, TC+1):
    q = []
    V, T = map(int, input().split())
    for i in range(pow(2, N)):
        p = bit(i)
        water = 0
        money = 0
        for j in p:
            water += damn[j][0]*T
            money += damn[j][1]
        
        if water >= V:
            push(q, money)


    if q:
        print(f'Case {tc}: {pop(q)}')
    else:
        print(f'Case {tc}: IMPOSSIBLE')
    