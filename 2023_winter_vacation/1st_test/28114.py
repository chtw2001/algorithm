from heapq import heappush as push, heappop as pop

_list = [input().split() for _ in range(3)]
year_list = []
for person in _list:
    push(year_list, int(person[1])%100)

year_answ = ''
for _ in range(3):
    year_answ += str(pop(year_list))

name_answ = []
for person in _list:
    push(name_answ, (-int(person[0]), person[2][0]))

name = ''
for _ in range(3):
    name += pop(name_answ)[1]

print(year_answ)
print(name)