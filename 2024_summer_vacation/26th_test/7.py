import sys
input = sys.stdin.readline

ary = [] # [0] => 백 
         # [1] => 흑
         
try:
    while True:
        ary.append(list(map(int, input().split())))
except:
    pass

N = len(ary)
dp = [[[0]*15 for _ in range(15)] for _ in range(N)]

