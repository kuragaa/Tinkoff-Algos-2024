import sys

def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())
left = 0 
right = n+1
ch = ' '
while right - left > 1:
    mid = (left + right) // 2
    ch = query(mid)
    if ch == '>=':
        left = mid
    elif ch == '<':
        right = mid

print('!', left)