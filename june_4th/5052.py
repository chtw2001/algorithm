from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    tc = int(input())
    phone_book = []
    dict = defaultdict(int)
    for _ in range(tc):
        ex = input().strip()
        phone_book.append(ex)
        dict[ex] += 1
    
    out = 0
    for phone in phone_book:
        dict[phone] -= 1
        for i in range(1, len(phone)+1):
            if dict[phone[:i]]:
                print("NO")
                out = 1
                break
        dict[phone] += 1
        if out:
            break
    if not out:
        print("YES")