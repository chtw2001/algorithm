from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(m)]
answ = [1]*n        # 모든 파티의 배열 1이면 거짓말 할 수 있는 파티
answ.insert(0,0)

q = defaultdict(set)   # {사람: set(파티번호)}
maze = [0]*(n+1)       # 0이면 모르는사람 1이면 아는사람


print(min(sum(answ), len(party)))