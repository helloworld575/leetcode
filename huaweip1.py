#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    max_part = int(sys.stdin.readline().strip())
    insert_part = int(sys.stdin.readline().strip())
    data_all = []
    print(max_part,insert_part)
    while(True):
        a = sys.stdin.readline().strip()
        if a=='end':
            break
        ans =a.split(",")
        data_all.append([int(ans[0]),int(ans[1])])
    for i in range(len(data_all)):
        if data_all[i][0]!=0:
            if data_all[i][0]>=insert_part:
                data_all[i][0]-=insert_part
                insert_part = 0
                break
            if data_all[i][0]<insert_part:
                insert_part = insert_part - data_all[i][0]
                data_all[i][0] = 0
    if insert_part==0:
        for i,j in data_all:
            print(str(i)+","+str(j))
    else:
        while insert_part>max_part:
            print("0"+","+str(max_part))
            insert_part=insert_part-max_part
        print("0"+","+str(insert_part))
        for i, j in data_all:
            print(str(i) + "," + str(j))
