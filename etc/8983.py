import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shoot = sorted(list(map(int, input().split())))
animal = [list(map(int, input().split())) for _ in range(n)]

answ = 0
for i, j in animal:
    start, end = 0, m-1
    while start <= end:
        mid = (start + end) // 2
        if shoot[mid] < i:
            start = mid + 1
        elif i < shoot[mid]:
            end = mid - 1
        else:
            if j <= l:
                answ += 1
            break

    if i != shoot[mid]:
        if 0 <= start <= m-1 and 0 <= end <= m-1:
            if min(abs(shoot[start] - i), abs(shoot[end] - i)) + j <= l:
                answ += 1
        else:
            if min(abs(shoot[0] - i), abs(shoot[m-1] - i)) + j <= l:
                answ += 1

print(answ)