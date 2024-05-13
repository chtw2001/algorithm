# 점프
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
small_ston = set()
for _ in range(M):
    small_ston.add(int(input()))

dp = [[0]*(N+1) for _ in range(N+1)]


