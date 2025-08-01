n = int(input())
s = input()
cnt = [0]*26
for ch in s:
    i = ord(ch) - ord('A')
    cnt[i] += 1
left = ''
right = ''
for i in range(26):
    while cnt[i] >= 2:
        left += chr(ord('A') + i)
        right += chr(ord('A') + i)
        cnt[i] -= 2
mid = ''
for i in range(26):
    if cnt[i] >= 1:
        mid += chr(ord('A') + i)
        break
res = left + mid + right[::-1]
print(res.strip())