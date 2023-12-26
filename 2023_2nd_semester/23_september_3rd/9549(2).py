import sys
from collections import defaultdict
input = sys.stdin.readline

def check(_origin, _pwd): # compare with origin, pwd dict
    for i in range(26):
        a, b = _dict[chr(97+i)], __dict[chr(97+i)]
        if a != b:
            return 0
    return 1 


TC = int(input())
for _ in range(TC):
    pwd = list(map(str, input().strip()))
    origin = list(map(str, input().strip()))
    len_origin, len_pwd = len(origin), len(pwd)

    _dict = defaultdict(int) # origin dict
    for alphabet in origin:
        _dict[alphabet] += 1 
    
    __dict = defaultdict(int) # pwd dict
    for alphabet in pwd[:len_origin-1]:
        __dict[alphabet] += 1
    flag = 0

    for i in range(len_origin-1, len_pwd): 
        __dict[pwd[i]] += 1
        if check(_dict, __dict):
            print('YES')
            flag = 1
            break
        __dict[pwd[i-len_origin+1]] -= 1
        
    if flag:
        continue
    else:
        print('NO')
    