from heapq import heappush as push, heappop as pop
import sys

input = sys.stdin.readline
T = int(input())

while T:
    M = int(input())
    ary = []
    for i in range(M//10 + 1):
        ary += list(map(int, input().split()))

    max_heap, min_heap, answ_ary = [], [], []
    
    for i in range(M):
        if (i+1) % 2: # odd num push max_heap
            push(max_heap, -ary[i])
            if min_heap and -max_heap[0] > min_heap[0]: # idx error cause
                push(min_heap, -pop(max_heap))
                push(max_heap, -pop(min_heap))
            answ_ary.append(-max_heap[0])
            
        else:
            push(min_heap, ary[i])
            if -max_heap[0] > min_heap[0]:
                push(min_heap, -pop(max_heap))
                push(max_heap, -pop(min_heap))
                # answ_ary.append(-max_heap[0])
    
    # cnt = 0
    # for i in range(M//2 + 1):
    #     cnt += 1
    #     print(answ_ary[i], end=' ')
    #     if not cnt % 10:
    #         cnt = 0
    #         print()
    answ_len = M//2 + 1
    print(answ_len)
    
    for i in range(0, answ_len, 10):  # 중앙값 리스트10개씩 쪼깨
            print(*answ_ary[i:i+10])  # 현재 구간의 중앙값출력하기
    
    T -= 1