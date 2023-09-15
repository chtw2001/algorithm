import sys
input = sys.stdin.readline

n = int(input())
row, column = map(int, input().split())
maze = sorted([list(map(int, input().split())) for _ in range(n)])

def check(ary, target):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end)//2
        if ary[mid] < target:
            start = mid + 1
        elif ary[mid] > target:
            end = mid - 1
        else:
            return 1

answ = 0
for i in maze:
    if not check(maze, [i[0]+row, i[1]+column]): # (x+row, y+column)인 점
        continue

    if not check(maze, [i[0]+row, i[1]]): # (x+row, y)인 점
        continue
    
    if not check(maze, [i[0], i[1]+column]): # (x, y+column)인 점
        continue
    
    answ += 1

print(answ)