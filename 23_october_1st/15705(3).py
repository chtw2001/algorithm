import sys
from collections import deque
input = sys.stdin.readline

string = input().strip()
length = len(string)
N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

def row(x, y):
    ex = ''
    for i in range(length):
        try:
            if y+i >= M:
                return 0
            ex += maze[x][y+i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def column(x, y):
    ex = ''
    for i in range(length):
        try:
            if x+i >= N:
                return 0
            ex += maze[x+i][y]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def r_row(x, y):
    ex = ''
    for i in range(length):
        try:
            if y-i < 0:
                return 0
            ex += maze[x][y-i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def r_column(x, y):
    ex = ''
    for i in range(length):
        try:
            if x-i < 0:
                return 0
            ex += maze[x-i][y]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def diagonal(x, y):
    ex = ''
    for i in range(length):
        try:
            if x+i >= N or y+i >= M:
                return 0
            ex += maze[x+i][y+i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def r_diagonal(x, y):
    ex = ''
    for i in range(length):
        try:
            if x-i < 0 or y-i < 0:
                return 0
            ex += maze[x-i][y-i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def r_r_diagonal(x, y):
    ex = ''
    for i in range(length):
        try:
            if x-i < 0 or y+i >= M:
                return 0
            ex += maze[x-i][y+i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

def r_r_r_diagonal(x, y):
    ex = ''
    for i in range(length):
        try:
            if x+i >= N or y-i < 0:
                return 0
            ex += maze[x+i][y-i]
        except:
            return 0
    if ex == string:
        return 1
    return 0

for i in range(N):
    for j in range(M):
        if row(i, j):
            print(1)
            quit()
        if r_row(i, j):
            print(1)
            quit()
        if column(i, j):
            print(1)
            quit()
        if r_column(i, j):
            print(1)
            quit()
        if diagonal(i, j):
            print(1)
            quit()
        if r_diagonal(i, j):
            print(1)
            quit()
        if r_r_diagonal(i, j):
            print(1)
            quit()
        if r_r_r_diagonal(i, j):
            print(1)
            quit()
print(0)