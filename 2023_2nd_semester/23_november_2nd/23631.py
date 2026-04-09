import sys
input = sys.stdin.readline

def check(s, e, n, k):
    if s >= e:
        return s
    mid = (s + e) // 2

    if mid*(mid+1)*k//2 >= n:
        return check(s, mid, n, k)
    else:
        return check(mid + 1, e, n, k)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    idx = check(0, 5000, N, K)

    distance = idx*(idx+1)//2

    if idx % 2 != 0:
        x = K*(idx//2+1)
        x += (N-1)-distance*K
        print(x, 'R')
    else:
        x = -K*(idx//2)
        x -= (N-1)-distance*K
        print(x, 'L')
        
# ref => https://lbdiaryl.tistory.com/222