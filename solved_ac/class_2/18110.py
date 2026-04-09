import sys
input = sys.stdin.readline

def round_up(num):
    if num - int(num) >= 0.5:
        return int(num + 1)
    return int(num)


N = int(input())
if not N:
    print(0)
    quit()

score = [int(input()) for _ in range(N)]
score.sort()
cutoff = round_up(N*0.15)

sum = 0
for i in range(cutoff, N-cutoff):
    sum += score[i]

print(round_up(sum/(N-(2*cutoff))))