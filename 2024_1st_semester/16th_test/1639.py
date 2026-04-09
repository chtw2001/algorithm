# 1번

string = list(map(int, input()))
length = len(string)
psum = [0]*(length + 1)
for i in range(length):
    psum[i+1] = psum[i]+string[i]

answ = 0
for i in range(1, length):
    size = min(i, length - i)
    for j in range(size):
        left_sum = psum[i] - psum[i-j-1]
        right_sum = psum[i+j+1] - psum[i]
        if left_sum == right_sum:
            answ = max(answ, j+1)

print(answ*2)
