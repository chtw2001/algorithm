import sys
input = sys.stdin.readline

TC = 0
while True:
    TC += 1
    N = int(input())
    if not N:
        quit()
    
    chain = dict()
    for _ in range(N):
        _from, _to = map(str, input().split())
        chain[_from] = _to
    
    answ = 0
    visited = set()
    for name in chain.keys():
        if name in visited:
            continue
        visited.add(name)
        target = chain[name]
        while target not in visited:
            visited.add(target)
            target = chain[target]
        
        answ += 1

    print(TC, answ)