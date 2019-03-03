import sys
def judge(n):
    pre = 1
    now = 1
    for i in range(2,n+1):
        tmp = now
        now = pre+now
        pre = tmp
    return now
def judge1(n,m):
    if n==1 or n==0:
        return 1
    else:
        sum =0
        for i in range(1,n+1):
            if i<=m:
                sum+=judge1(n-i,m)
        return sum
for line in sys.stdin:
    a = line.split()
    if int(a[1])==1:
        print(1)
    else:
        print(judge1(int(a[0]),int(a[1]))%10007)
