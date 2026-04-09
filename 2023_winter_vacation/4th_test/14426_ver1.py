# 3번
# 접두사 찾기 (깡)
# N개의 문자열이 주어짐
# 이전에 주어진 N개의 문자열이 이 후에 주어질 
# M개의 문자열을 접두사로 하는 문자열의 개수 출력
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin = [input().strip() for _ in range(N)]
check = [input().strip() for _ in range(M)]

union = set()
for string in origin:
    ex = ''
    for alpha in string:
        ex += alpha
        union.add(ex)
        
answ = 0
for string in check:
    if string in union:
        answ += 1
        
print(answ)