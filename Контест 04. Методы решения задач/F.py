n = int(input())
points = []

for _ in range(n):
    left, right = map(int, input().split())
    points.append((left, 'start'))
    points.append((right, 'end'))
points.sort()

length = 0
intersect = 0

for i in range(len(points)):
    if points[i][1] == 'start':
        intersect += 1
    else:
        intersect -= 1
    if intersect > 0: 
        length += points[i + 1][0] - points[i][0]

print(length)