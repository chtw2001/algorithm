k, l, n = map(int, input().split())
ary = list(map(int, input()))

flush = []
idx = 0
using = [0,0] # 0 => switch, 1 => during
unusing = 0

while idx < n+l:
    try:
        if ary[idx]:
            using[1] += 1
            unusing = 0
            if using[1] >= k:
                using[0] = 1
            
        else:
            using[1] = 0
            unusing += 1
            if unusing >= l and using[0]:
                flush.append(idx+1)
                unusing = 0
                using = [0,0]
            
        idx += 1
    except:
        if using[0] and unusing + n - idx >= 0: # origin => unsing + (n + l) - idx >= l
            flush.append(n+l)
        
        break
        
if flush:
    for i in flush:
        print(i)
else:
    print('NIKAD')