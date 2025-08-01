def dfs(i, j, dmg, size):
    if i >= N or j >= M or i < 0 or j < 0:
        return dmg, size
    if visited[i][j]:
        return dmg, size
    visited[i][j] = True
    if field[i][j] == '#' or field[i][j] == 'X':
        size += 1
        if field[i][j] == 'X':
            dmg += 1
        dmg, size = dfs(i - 1, j, dmg, size)
        dmg, size = dfs(i + 1, j, dmg, size)
        dmg, size = dfs(i, j - 1, dmg, size)
        dmg, size = dfs(i, j + 1, dmg, size)
    return dmg, size


N, M = map(int, input().split())
counter = {
    "alive" : 0,
    "damaged" : 0,
    "destroyed" : 0,
}
field = []
for i in range(N):
    s = " ".join(input())
    field.append(s.split())
visited = [[False for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        dmg, size = 0, 0
        dmg, size = dfs(i, j, dmg, size)
        if size > 0:
            if dmg == size:
                counter['destroyed'] += 1
            elif dmg == 0:
                counter['alive'] += 1
            else:
                counter['damaged'] += 1
print(*counter.values())