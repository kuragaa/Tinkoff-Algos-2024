from collections import deque

n = int(input())
start = tuple(map(int, input().split()))
goal = tuple(map(int, input().split()))

visited = dict()
visited[start] = (-1, -1)
moves = ((1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1))
q_bfs = deque()
q_bfs.append(start)

while q_bfs:
    coords = q_bfs.popleft()
    for x, y in moves:
        new = coords[0] + x, coords[1] + y
        if (0 < new[0] <= n and 0 < new[1] <= n) and new not in visited:
            visited[new] = coords
            q_bfs.append(new)
            if new == goal:
                break

path = [(goal[0], goal[1])]
coords = goal
while visited[coords][0] != -1:
    path.append(visited[coords])
    coords = visited[coords]

print(len(path) - 1)
for coord in reversed(path):
    print(coord[0], coord[1])