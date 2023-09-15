n = int(input())
ary = [0]
for _ in range(n):
    ary.append(int(input()))
    
def move(i, set):
    if ary[i] in set:
        return len(set)
    set.add(ary[i])
    return move(ary[i], set)

# maximize the number of people
answ = 0
_max = -1
for i in range(1, n+1):
    ex = move(i, {i})
    if ex > _max:
        _max = ex
        answ = i

print(answ)