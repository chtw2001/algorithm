import sys
input = sys.stdin.readline
tc = int(input())

nearby = [[7], [2, 4], [1, 3, 5], [2, 6], 
          [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], 
          [4, 8, 0], [5, 7, 9], [6, 8]]

for _ in range(tc):
    n = int(input())
    key = [1]*10
    
    for i in range(1, n) :
        value = dict()
        for j in range(10):
            value[j] = key[j]

        for j in range(10):
            ex = 0
            for k in nearby[j]:
                ex += value[k]
            key[j] = ex

    answ = 0
    for num in key:
        answ += num
        
    print(answ % 1234567)