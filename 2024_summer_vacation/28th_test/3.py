import sys
input = sys.stdin.readline

TC = int(input())
cnt = 1
while cnt <= TC:
    ary = [list(map(int, input().split())) for _ in range(9)]
    if cnt != TC:
        space = input()
    
    flag = 0
    for i in range(9):
        ex = set()
        for j in range(9):
            if ary[i][j] in ex:
                flag = 1
                break
            ex.add(ary[i][j])
        if flag:
            break
    
    if not flag:
        for i in range(9):
            ex = set()
            for j in range(9):
                if ary[j][i] in ex:
                    flag = 1
                    break
                ex.add(ary[j][i])
            if flag:
                break
    
    if not flag:
        ex_ary = [[set(), set(), set()] for _ in range(3)]
        for i in range(9):
            if i < 3:
                for j in range(9):
                    if j < 3:
                        if ary[i][j] in ex_ary[0][0]:
                            flag = 1
                            break
                        ex_ary[0][0].add(ary[i][j])
                    elif j < 6:
                        if ary[i][j] in ex_ary[0][1]:
                            flag = 1
                            break
                        ex_ary[0][1].add(ary[i][j])
                    else:
                        if ary[i][j] in ex_ary[0][2]:
                            flag = 1
                            break
                        ex_ary[0][2].add(ary[i][j])

                if flag:
                    break
                    
            elif i < 6:
                for j in range(9):
                    if j < 3:
                        if ary[i][j] in ex_ary[1][0]:
                            flag = 1
                            break
                        ex_ary[1][0].add(ary[i][j])
                    elif j < 6:
                        if ary[i][j] in ex_ary[1][1]:
                            flag = 1
                            break
                        ex_ary[1][1].add(ary[i][j])
                    else:
                        if ary[i][j] in ex_ary[1][2]:
                            flag = 1
                            break
                        ex_ary[1][2].add(ary[i][j])
                        
                if flag:
                    break
            else:
                for j in range(9):
                    if j < 3:
                        if ary[i][j] in ex_ary[2][0]:
                            flag = 1
                            break
                        ex_ary[2][0].add(ary[i][j])
                    elif j < 6:
                        if ary[i][j] in ex_ary[2][1]:
                            flag = 1
                            break
                        ex_ary[2][1].add(ary[i][j])
                    else:
                        if ary[i][j] in ex_ary[2][2]:
                            flag = 1
                            break
                        ex_ary[2][2].add(ary[i][j])
                        
                if flag:
                    break
                    
    if flag:
        print(f'Case {cnt}: INCORRECT')
    else:
        print(f'Case {cnt}: CORRECT')
    cnt += 1
    
