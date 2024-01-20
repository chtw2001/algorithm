# 접두사 찾기 (이분탐색)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_ = [input().rstrip() for _ in range(N)]
str_ = [input().rstrip() for _ in range(M)]

list_.sort()

cnt = 0
for string in str_:
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if list_[mid].startswith(string):
            cnt += 1
            break
        elif list_[mid] < string:
            start = mid + 1
        else:
            end = mid - 1

print(cnt)