import sys
input = sys.stdin.readline

N = int(input())
id = [int(input()) for _ in range(N)]
length = len(str(id[0]))

for i in range(length):
    flag = 0
    union = set()
    for p in id:
        ex = p % pow(10, i+1)
        if ex in union:
            flag = 1
            break
        union.add(ex)

    if flag:
        continue
    else:
        print(i+1)
        quit()