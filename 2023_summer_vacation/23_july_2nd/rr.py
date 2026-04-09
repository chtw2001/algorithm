import sys
from collections import defaultdict
input = sys.stdin.readline

dict = defaultdict(int)
answ = 0
n = int(input())

while n > 0:
    input_data = input().strip()
    if input_data == 'ENTER':
        n -= 1
        dict = defaultdict(int)
        continue

    if not dict[input_data]:
        dict[input_data] += 1
        answ += 1
        
    n -= 1

print(answ)