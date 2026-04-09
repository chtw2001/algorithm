# 5번 경로 찾기
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
move = [[0, 1], [1, 0]]
game = defaultdict(int)
for i in range(1, C+1):
    x, y = map(int, input().split())
    game[(x, y)] = i

path = [[0]*(C+2) for _ in range(C+2)] # [0] => start, [C+1] => end
game_keys = set(game.keys())

def calculate_path(start, end, target):
    table = [[0]*(M+1) for _ in range(N+1)]
    table[start[0]][start[1]] = 1
    for x in range(1, N+1):
        for y in range(1, M+1):
            if (x, y) in game_keys and game[(x, y)] not in target:
                continue
            if x + 1 <= N:
                table[x + 1][y] += table[x][y]
                table[x + 1][y] %= 1000007
            if y + 1 <= M:
                table[x][y + 1] += table[x][y]
                table[x][y + 1] %= 1000007
                
    return table[end[0]][end[1]] % 1000007

# start => end
path[0][C+1] = calculate_path((1, 1), (N, M), {})

# start => game
for i in game_keys:
    if i == (1, 1):
        path[0][game[i]] = 0
        continue
    path[0][game[i]] = calculate_path((1, 1), i, {game[i]})

# game => game
for i in game_keys:
    for j in game_keys:
        if i == j:
            continue
        path[game[i]][game[j]] = calculate_path(i, j, {game[i], game[j]})

# game => end
for i in game_keys:
    if i == (N, M):
        path[game[i]][C+1] = 0
        continue
    path[game[i]][C+1] = calculate_path(i, (N, M), {game[i]})

def combinations(n, k):
    result = []
    combination = []

    def backtrack(start, k):
        if k == 0:
            result.append(combination[:])
            return
        for i in range(start, n + 1):
            combination.append(i)
            backtrack(i + 1, k - 1)
            combination.pop()

    backtrack(1, k)
    return result

print(path[0][C+1], end=' ')
for r in range(1, C+1):
    answ = 0
    for tuple in combinations(C, r):
        start = 0
        ex = 1
        for j in tuple:
            ex *= path[start][j]
            start = j
        ex *= path[start][C+1]
        answ += ex
    print(answ%1000007, end=' ')
