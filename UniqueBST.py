
# 这是一个数学问题 96
def numTrees(n):
    a = [0]*(n+1)

    a[0] = a[1] = 1

    for i in range(2,n+1):
        for j in range(1,i+1):
            a[i]+=a[j-1]*a[i-j]

    return a[n]

print(numTrees(3))