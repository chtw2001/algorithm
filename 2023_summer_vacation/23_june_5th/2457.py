from heapq import heappush as push, heappop as pop
import sys
input = sys.stdin.readline

n = int(input())
DoM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 3/1 => 60
# 12/1 => 335
def date_change(ary):
    s_date = ary[1]
    for i in range(ary[0]):
        s_date += DoM[i]
    e_date = ary[3]
    for i in range(ary[2]):
        e_date += DoM[i]
    return [s_date, e_date]
    
flower = []
for _ in range(n):
    ex = date_change(list(map(int, input().split())))
    push(flower, ex)

answ = 0
end = 60
while flower:
    if flower[0][0] > end:
        print(0)
        quit()
        
    if flower[0][1] > end:
        ex = pop(flower)
    else:
        continue
    
    
    
    
    
    