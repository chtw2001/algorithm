from collections import defaultdict

N, M = map(int, input().split())
_truth = list(map(int, input().split())) # idx[0] => # of truth
truth_party = [1]*M

dict_party = defaultdict(set) # key : party idx, value : party people
dict_people = defaultdict(set) # key : party people, value : party idx
for i in range(M):
    ex = list(map(int, input().split()))
    for p in ex[1:]:
        dict_people[p].add(i)
        dict_party[i].add(p)


def dfs(idx, visited): # person's idx, visited set
    for party in dict_people[idx]:
        if (idx, party) in visited:
            continue
        visited.add((idx, party))
        truth_party[party] = 0
        for people in dict_party[party]:
            if (people, party) in visited:
                continue
            dfs(people, visited)
    

visited = set()
for i in _truth[1:]:
    dfs(i, visited)

answ = 0
for i in truth_party:
    answ += i
print(answ)
