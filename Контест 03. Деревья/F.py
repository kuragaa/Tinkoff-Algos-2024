class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


n = int(input())
head = None
y = 0
for i in range(n):
    s = input().split()
    temp = (y + int(s[1])) % 10 ** 9
    if s[0] == '+':
        if not head:
            head = Node(temp)
        else:
            tm = head
            while tm:
                if temp > tm.x and tm.right:
                    tm = tm.right
                elif temp < tm.x and tm.left:
                    tm = tm.left
                else:
                    break
            if temp > tm.x:
                tm.right = Node(temp)
            elif temp < tm.x:
                tm.left = Node(temp)
        y = 0
    else:
        tm = head
        temp = int(s[1])
        diff = 2 * 10 ** 9
        flag = False
        while tm:
            if tm.x - temp == 0:
                diff = 0
                flag = True
                break
            if temp - tm.x < 0:
                if (diff > tm.x - temp):
                    diff = tm.x - temp
                    flag = True
                tm = tm.left
            elif temp - tm.x > 0:
                tm = tm.right
        if flag:
            print(temp + diff)
            y = temp + diff
        else:
            print("-1")