n, cost = map(int, input().split())
problems = list()
for i in range(1, n+1):
    start, time = map(int, input().split())
    problems.append((start, start+time, i))
problems.sort(key=lambda x: x[1])

res = []
problem = problems[0]
res.append(problem[2])
stop = problem[1]
for i in range(1, len(problems)):
    problem = problems[i]
    start = problem[0]
    end = problem[1]
    if start >= stop:
        res.append(problem[2])
        stop = end
print(len(res)*cost)
print(len(res))
print(*res)