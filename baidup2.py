import sys
import math
if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip()
    m,a,b,c,d = list(map(int,n.split()))
    arr = []
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        arr.append(values)
    p1 = [a,b]
    p2 = [c,d]
    r1 = 0
    r2 = 0
    for point in arr:
        #计算两个中心到点的距离
        d1 = math.sqrt((point[0]-p1[0])*(point[0]-p1[0])+(point[1]-p1[1])*(point[1]-p1[1]))
        d2 = math.sqrt((point[0]-p2[0])*(point[0]-p2[0])+(point[1]-p2[1])*(point[1]-p2[1]))
        if d1>r1 and d2>r2:
            if (d1*d1+r1*r1)>(r1*r1+d2*d2):
                r2 = d2
            else:
                r1 = d1
    print(int(r1*r1+r2*r2))

