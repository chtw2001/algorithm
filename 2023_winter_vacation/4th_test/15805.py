# 4번
# 트리 나라 관광 가이드
# 전위순회 결과가 입력으로 주어짐
# 0 ~ K-1 개의 도시 순서대로 부모 노드를 출력해야함
N = int(input())
ary = list(map(int, input().split()))

visited = set()
prev = -1
i = 0
answ = [0]*N
length = len(set(ary))
print(length)
while i < N:
    if ary[i] in visited:
        prev = ary[i]
        i += 1
        continue
    visited.add(ary[i])
    answ[ary[i]] = prev
    prev = ary[i]
    i += 1

print(*answ[:length])