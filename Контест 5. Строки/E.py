n = input()
s = input()
s1 = len(s)
s2 = len(n)
cnt1 = 0
k_ner = False
len_pods = 0
ans = []
k = s1 - s2 + 1

for j in range(k):
    for cnt1 in range(j, s1):
        if s[cnt1] == n[len_pods]:
            len_pods += 1
        elif s[cnt1] != n[len_pods]:
            if k_ner:
                k_ner = False
                len_pods = 0
                break
            k_ner = True
            len_pods += 1
        if len_pods == s2:
            ans.append(cnt1 - len_pods + 2)
            len_pods = 0
            k_ner = False
            break

print(len(ans))
print(*ans)