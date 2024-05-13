# 2번 민겸 수
num = input()
length = len(num)
i = 0
mflag, kflag = 0, 0
if num[-1] == 'K':
    kflag = 1
max_list = []
while i < length:
    if num[i] == 'M':
        mflag += 1
    else:
        max_list.append(str(5 * pow(10, max(0, mflag))))
        mflag = 0
    i += 1

if not kflag:
    for i in range(mflag):
        max_list.append('1')

max_num = int(''.join(max_list))

i = 0
mflag = 0
min_list = []
while i < length:
    if num[i] == 'M':
        mflag += 1
    else:
        if mflag:
            min_list.append(str(pow(10, max(0, mflag-1))))
        min_list.append('5')
        mflag = 0
    i += 1

if not kflag:
    min_list.append(str(pow(10, max(0, mflag-1))))

min_num = int(''.join(min_list))
print(max_num)
print(min_num)