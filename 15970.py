import sys
input = sys.stdin.readline

n = int(input())
ary = {}
dot = [list(map(int, input().split())) for _ in range(n)]
for i, j in dot:
    ary[j] = []

for i, j in sorted(dot):
    ary[j].append(i)

answ = 0
for i in ary.keys():
    for j in range(len(ary[i])):
        if j == 0 and len(ary[i]) > 1:
            answ += abs(ary[i][j] - ary[i][j+1])
        elif j == len(ary[i])-1 and len(ary[i]) > 1:
            answ += abs(ary[i][j] - ary[i][j-1])
        else:
            answ += min(abs(ary[i][j] - ary[i][j+1]), abs(ary[i][j] - ary[i][j-1]))
        
print(answ)