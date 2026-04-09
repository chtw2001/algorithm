import sys
input = sys.stdin.readline
from collections import defaultdict

DNA = ['A', 'C', 'G', 'T']

def check(c):
    for i in DNA: # time complexity O(4*P), P: 10^6
        if c[i][0] > c[i][1]:
            return 0

    return 1

S, P = map(int, input().split())
string = list(input().strip())
dict = defaultdict(int)

A, C, G, T = map(int, input().split())
dict['A'] = [A, 0]
dict['C'] = [C, 0]
dict['G'] = [G, 0]
dict['T'] = [T, 0]


for i in range(P):
    dict[string[i]][1] += 1

answ = check(dict)
start = 0
for i in range(P, S):
    dict[string[start]][1] = max(0, dict[string[start]][1] - 1)
    dict[string[i]][1] += 1
    answ += check(dict)
    start += 1
    
print(answ)