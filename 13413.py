import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    length = int(input())
    maze = input().strip()
    maze2 = input().strip()

    w, b = 0, 0
    for i in range(length):
        if maze[i] != maze2[i]:
            if maze[i] == 'W':
                w += 1
            else:
                b += 1
    print(max(w, b))