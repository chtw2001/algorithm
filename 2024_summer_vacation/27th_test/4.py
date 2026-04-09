import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

table = [[0]*10 for _ in range(10)]
table[1][3] = 2
table[1][7] = 4
table[1][9] = 5
table[2][8] = 5
table[3][1] = 2
table[3][7] = 5
table[3][9] = 6
table[4][6] = 5
table[6][4] = 5
table[7][1] = 4
table[7][3] = 5
table[7][9] = 8
table[8][2] = 5
table[9][1] = 5
table[9][3] = 6
table[9][7] = 8

pre = {ary[0]}
for i in range(1, N):
    if ary[i] in pre:
        print("NO")
        quit()
        
    if table[ary[i-1]][ary[i]]:
        pre.add(table[ary[i-1]][ary[i]])
        
    pre.add(ary[i])

for i in ary:
    pre.discard(i)

if pre:
    print("NO")
else:
    print("YES")
