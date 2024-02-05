# 1번 메시지
import sys
input = sys.stdin.readline

group = 1
while True:
    N = int(input())
    if not N:
        break
    msg = [list(input().split()) for _ in range(N)]
    sentense = ' was nasty about '
    
    list_ = []
    for i in range(N): # O(N)
        idx = 1
        for j in range(1, N): # O(N)
            if msg[i][idx] == 'N':
                list_.append((msg[i-j][0] ,msg[i][0]))
            idx += 1
    
    print(f'Group {group}')
    if not list_:   # O(N)
        print('Nobody was nasty')
    else:
        for nasty, nastyed in list_:
            print(nasty + sentense + nastyed)
    print()
    group += 1

# O(N^2)