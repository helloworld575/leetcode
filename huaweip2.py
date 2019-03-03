#coding=utf-8
import sys
if __name__ == "__main__":
    data_all = []
    while(True):
        a = sys.stdin.readline().strip()
        if a=='0,0':
            break
        ans =a.split(",")
        data_all.append([int(ans[0]),int(ans[1])])
    time = 21-8
    for i in range(len(data_all)):
        for j in range(i,len(data_all)):
            if (data_all[i][1]-data_all[i][0])<(data_all[j][1]-data_all[j][0]):
                temp = data_all[i]
                data_all[i] = data_all[j]
                data_all[j] = temp
            elif (data_all[i][1]-data_all[i][0])==(data_all[j][1]-data_all[j][0]) and (data_all[i][0]>data_all[j][0]):
                temp = data_all[i]
                data_all[i] = data_all[j]
                data_all[j] = temp
    ans = [data_all[0]]
    for i in range(1,len(data_all)):
        flag = True
        for j in ans:
            if (j[0]<data_all[i][0] and j[1]>data_all[i][0]) or (j[0]<data_all[i][1] and j[1]>data_all[i][1]):
                flag=False
        if flag:
            ans.append(data_all[i])
    for i in range(len(ans)):
        for j in range(i,len(ans)):
            if ans[i][1]>ans[j][1]:
                temp = ans[i]
                ans[i] = ans[j]
                ans[j] = temp
    for i,j in ans:
        print(str(i)+","+str(j))

