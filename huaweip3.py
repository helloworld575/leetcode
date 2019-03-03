#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
import collections
if __name__ == "__main__":
    # 读取第一行的n
    ans = []
    for i in range(10):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = []
        for i in line:
            value.append(i)
        ans.append(value)
    i = int(sys.stdin.readline().strip())
    j = int(sys.stdin.readline().strip())
    paths = collections.deque([[i,j]])
    flag = False
    while paths:
        t = paths.pop()
        i = t[0]
        j = t[1]
        if i==0 or i==9 or j==0 or j==9:
            print(1)
            flag = True
            break
        ans[i][j]=1
        if ans[i][j+1]=='0':
            paths.append([i,j+1])
        if ans[i][j-1]=='0':
            paths.append([i,j-1])
        if ans[i+1][j]=='0':
            paths.append([i+1,j])
        if ans[i-1][j]=='0':
            paths.append([i-1,j])
    if not flag:
        print(0)
