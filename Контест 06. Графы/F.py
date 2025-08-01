from collections import defaultdict, deque

m = int(input())
reactions = defaultdict(list)

for _ in range(m):
    fr, to = input().split(" -> ")
    reactions[fr].append(to)

el1 = input()
el2 = input()
path_len = {el1: 0}
q_bfs = deque([el1])


while q_bfs:
    cur = q_bfs.popleft()
    if cur == el2:
        print(path_len[cur])
        break
    for el in reactions[cur]:
        if el not in path_len:
            path_len[el] = path_len[cur] + 1
            q_bfs.append(el)
else:
    print(-1)