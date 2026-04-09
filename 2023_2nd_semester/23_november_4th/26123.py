from collections import defaultdict

N, D = map(int, input().split())
dict = defaultdict(int)
top, answ = 0, 0
ary = list(map(int, input().split()))

for i in ary:
    dict[i] += 1
    top = max(top, i)
    
if not top:
    print(answ)
    quit()
    
for _ in range(D):
    dict[top-1] += dict[top]
    answ += dict[top]
    top -= 1
    if not top:
        print(answ)
        quit()

print(answ)