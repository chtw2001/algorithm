from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]
table = [[] for _ in range(n+1)]

