def postfix(arr, op):
    if op.isdigit():
        arr.append(int(op))
    if op == '+':
        arr.append(arr.pop() + arr.pop())
    elif op == '-':
        b = arr.pop()
        a = arr.pop()
        arr.append(a - b)
    elif op == '*':
        arr.append(arr.pop() * arr.pop())

op = list(input().split())
arr = []
for el in op:
    postfix(arr, el)
print(arr.pop())