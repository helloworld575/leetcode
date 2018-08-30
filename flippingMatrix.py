tog = [[0,1],[0,1],[0,1],[0,0]]

def matrixScore(tog):
    # 先转化行
    row = len(tog)
    column = len(tog[0])
    for r in range(row):

        if tog[r][0]==0:
            for c in range(column):
                if tog[r][c] ==0:
                    tog[r][c]=1
                else:
                    tog[r][c]=0
    print(row,column)
    #再转化列
    for c in range(1,column):
        num_1 = 0
        for r in range(row):
            if tog[r][c]==1:
                num_1 +=1
        print(num_1,row/2)
        if num_1<row/2:
            print("num_1:"+str(num_1))
            for r in range(row):
                if tog[r][c]==1:
                    tog[r][c]=0
                else:
                    tog[r][c]=1
    print(tog)
    # 计算大小
    sum = 0
    for r in range(row):
        for c in range(column):
            sum+=tog[r][c]*(2**(column-c-1))

    return sum
print(matrixScore(tog))