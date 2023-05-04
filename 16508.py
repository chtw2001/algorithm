from heapq import heappush as push, heappop as pop
from collections import defaultdict
import sys
input = sys.stdin.readline

t = input().strip()
book_n = int(input())
info = []

def check(origin, book): # book에는 해당 책의 딕셔너리 들어감
    string = []
    for i in origin:
        string.append(i)
        
    for i in origin:
        if i in string and book[i]:
            book[i] -= 1
            del string[string.index(i)]
    return string

for _ in range(book_n):
    price, name = map(str, input().split())
    dict = defaultdict(int)
    for i in name:
        dict[i] += 1
    info.append([int(price), dict])

answ = sys.maxsize
no_match = True
for i in range(1, pow(2, book_n)):
    ex = 0
    binary = bin(i)[2:][::-1]
    string = t
    for j in range(len(binary)):
        if int(binary[j]):
            dictionary = info[j][1].copy()
            string = check(string, dictionary)
            if string == t:
                pass
            elif not string:
                ex += info[j][0]
                break
            else:
                ex += info[j][0]
    if not string:
        no_match  = False
        answ = min(answ, ex)

if no_match:
    print(-1)
else:
    print(answ)