import sys
from collections import defaultdict
input = sys.stdin.readline

L = int(input())
N = int(input())
visitor = [list(map(int, input().split())) for _ in range(N)]
cake = [-1]*L

expected = -1
expected_person = 0
for i in range(N):
    p, k = visitor[i][0], visitor[i][1]
    ex = k-p+1
    if expected < ex:
        expected_person = i+1
        expected = ex
        
dict = defaultdict(int)

for i in range(N):
    p, k = visitor[i][0]-1, visitor[i][1]-1
    for j in range(p, k+1):
        if cake[j] != -1:
            continue
        cake[j] = i
        dict[i] += 1

fact = -1
fact_person = 0
for i in range(N):
    if fact < dict[i]:
        fact_person = i+1
        fact = dict[i]

print(expected_person)
print(fact_person)