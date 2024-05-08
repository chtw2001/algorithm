# 4번 문자 해독
from collections import defaultdict
g, s = map(int, input().split())
origin = defaultdict(int)
W = input().rstrip()
for i in W:
    origin[i] += 1

S = input().rstrip()

compare = defaultdict(int)
for i in range(g):
    compare[S[i]] += 1

W = set(W)
def check():
    for i in W:
        if origin[i] != compare[i]:
            return False
    return True


answ = 0
if check():
    answ += 1

for i in range(g, s):
    compare[S[i-g]] -= 1
    compare[S[i]] += 1
    if check():
        answ += 1

print(answ)
