# N = int(input())

# ary = ['2', '0', '2', '3']
# answ = 0
# for i in range(2023, N+1):
#     j = 0
#     length = len(str(i))
#     for ele in str(i):
#         if ele == ary[j]:
#             j += 1
#             if j == 4:
#                 answ += 1
#                 break

# print(answ)
N = int(input())

ary = [2, 0, 2, 3]
answ = 0
for i in range(2023, N+1):
    idx = 3
    num = i
    while i > 0:
        ex = i % 10
        if ex == ary[idx]:
            idx -= 1
        if idx == -1:
            answ += 1
            break
        i //= 10

print(answ)
