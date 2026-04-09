maze = input()

dict = {'northlondo': 'NLCS', 
       'branksomeh': 'BHA', 
       'koreainter': 'KIS',
       'stjohnsbur': 'SJA'}

for i in range(26):
    ex = ''
    for j in maze:
        if ord(j)+i > 122:
            ex += str(chr(ord(j)+i-26))
        else:
            ex += str(chr(ord(j)+i))
    try:
        if dict[ex]:
            print(dict[ex])
            quit()
    except:
        continue