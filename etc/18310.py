import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

if n == 2:
    print(min(arr))
    quit()
if n == 1:
    print(arr[0])
    quit()

home = [0]*(max(arr)+1)
for i in arr:   # how many houses in the location
    home[i] += 1
a_arr = [0]*(max(arr)+1)
answ = sys.maxsize

ex = 0
while True:
    ex += 1
    cnt = 0
    for i in range(1, max(arr)+1):
        if home[i] != 0:
            cnt += abs(i-ex)*home[i]
    if answ >= cnt:
        answ = cnt
        a_arr[ex] = cnt
    else:
        print(a_arr.index(answ))
        quit()