import sys
def judgeNum(N):
    a = [0]*N
    for i in range(2,N):
        if a[i]==0:
            for j in range(i+i,N,i):
                a[j]=1
    return a
def array(N):
    a = [0]
    for i in range(1,N):
        a.append(2*i-1)
    return a
for line in sys.stdin:
    a = line.split()
    print(a)
    N = int(a[0][2:])
    s = 0
    nums = judgeNum(2*N+1)
    myArray = array(N)
    for i in myArray:
        if nums[i]==0:
            s+=i
    print(s)