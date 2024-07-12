list = list(map(int, input().split()))
list.sort()

print( abs((list[0]+list[3]) - (list[1]+list[2])) )
