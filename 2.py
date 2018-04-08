#coding=utf-8
import sys

L = sys.stdin.readline().strip()
a = list((map(int, L.split())))
ans = 0
sum = 0
c=-1
for i in range(1,int(a[0]+1)):
    if sum<int(a[1]):
        c = c
    else:
        c = -1*c
        sum = 0
    sum += 1
    ans = ans+c*i
print(ans)