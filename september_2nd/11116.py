import sys
input = sys.stdin.readline

def binary_search(_list, t):
    t += 500
    s, e = 0, length - 1
    mid = (s + e) // 2

    while s <= e:
        mid = (s + e) // 2
        if _list[mid] < t:
            s = mid + 1
        elif t < _list[mid]:
            e = mid - 1
        else:
            return _list[mid]
    
    return 0


TC = int(input())
for _ in range(TC):
    answ = 0
    length = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    used = set()
    left_idx = 0

    while left_idx < length:
        if left[left_idx] in used:
            left_idx += 1
            continue
# do not insert early in set. 
        target = binary_search(left, left[left_idx])
        if target:
            target = binary_search(right, target)
            if target:
                target = binary_search(right, target)
                if target:
                    answ += 1
                    for i in range(4):
                        used.add(target*i)

        left_idx += 1

    print(answ)
