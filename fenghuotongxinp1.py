def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
num = int(input())
ans = []
for i in range(num):
    s = input()
    t = input()
    if isIsomorphic(s,t):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)