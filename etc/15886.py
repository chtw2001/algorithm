n = int(input())
m = list(input())

def check(ary, n):
    if ary[n] == 'W':
        return n-1
    return n+1

cnt = 0
global_set = set()

for i in range(n):
    if i in global_set:
        continue
    num = i
    local_set = set()
    while num not in local_set:
        local_set.add(num)
        num = check(m, num)
        if num in global_set:
            break
    if num in global_set:       # 합집합
        global_set = global_set.union(local_set)
        continue
    else:                       # 합집합
        global_set = global_set.union(local_set)
        cnt += 1
    
print(cnt)