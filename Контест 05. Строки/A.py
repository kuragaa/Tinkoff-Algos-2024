s = input()  
mod = 10**9 + 7
t = 31
len_s = len(s)
h_pref = [0] * (len_s + 1)  
p = [1] * (len_s + 1)  
for i in range(len_s):
    h_pref[i + 1] = (h_pref[i] * t + (ord(s[i]) - ord('a') + 1)) % mod  
for i in range(len_s):
    p[i + 1] = (p[i] * t) % mod 


n = int(input())
for _ in range(n):
    l, r, l1, r1 = map(int, input().split())
    s1 = (h_pref[r] - h_pref[l - 1] * p[r - l + 1]) % mod
    s2 = (h_pref[r1] - h_pref[l1 - 1] * p[r1 - l1 + 1]) % mod
    if s1 == s2:
        print('Yes')
    else:
        print('No')