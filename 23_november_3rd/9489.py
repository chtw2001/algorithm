import sys
input = sys.stdin.readline


while True:
    N, K = map(int, input().split())
    if not N and not K:
        break

    ary = list(map(int, input().split()))
    mapping = {}
    depth_cnt = 1
    i = 1
    depth = [[] for _ in range(N+1)]
    depth[0].append(ary[0])
    mapping[ary[0]] = -1

    while i < N:
        for k in range(len(depth[depth_cnt-1])):
            if i < N:
                parent = depth[depth_cnt-1][k]
                post_ele = ary[i]
                mapping[post_ele] = parent
                depth[depth_cnt].append(post_ele)

                while i + 1 < N:
                    if post_ele + 1 == ary[i+1]:
                        post_ele += 1
                        mapping[post_ele] = parent
                        depth[depth_cnt].append(post_ele)
                        i += 1
                    else:
                        break
                i += 1

        depth_cnt += 1

    parent = mapping[K]
    try:
        grandparent = mapping[parent]
    except:
        print(0)
        continue
    depth_num = 0
    for i in range(len(depth)):
        if K in depth[i]:
            depth_num = i
            break

    answ = 0
    for ele in depth[depth_num]:
        try:
            if mapping[ele] != parent and mapping[mapping[ele]] == grandparent:
                answ += 1
        except:
            continue

    print(answ)
