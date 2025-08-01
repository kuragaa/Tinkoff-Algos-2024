import sys

n = int(sys.stdin.readline().strip())
cnt2, cnt5 = 0, 0
ans = 1
for i in range(1, n + 1):
    num = i
    while num % 2 == 0:
        num //= 2
        cnt2 += 1
    while num % 5 == 0:
        num //= 5
        cnt5 += 1
    ans = (ans * num) % 10
for _ in range(cnt2 - cnt5):
    ans = (ans * 2) % 10

print(ans)