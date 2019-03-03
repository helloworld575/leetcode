#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def judge(t,str):
    i,j= 0,0
    while(j < len(str)):
        if t[i]==str[j]:
            i+=1
            j+=1
        else:
            j+=1
        if i==len(t)-1:
            return True
    return False

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    aType = []
    for i in range(n):
        # 读取每一行
        aType.append(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    contents = []
    for i in range(m):
        contents.append(sys.stdin.readline().strip())
    print(aType)
    print(contents)
    for str in contents:
        flag = False
        for t in aType:
            if judge(t,str):
                flag = True
                break
        if flag:
            print("YES")
        else:
            print("NO")