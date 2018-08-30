a = [[-1],[2,3],[1,-1,-3]]

def minimumTotal(triangle):
    # wrong answer
    # line = 1
    # column = 0
    # nSum = triangle[0][0]
    # while line<len(triangle):
    #     if triangle[line][column]>=triangle[line][column+1]:
    #         column = column+1
    #     nSum+=triangle[line][column]
    #     print(triangle[line][column])
    #     line+=1
    # return nSum
    # 想通了很有意思，从上往下想，如果用贪婪算法，总有不完善的地方，但是从下往上则不然，因为从下往上考虑到了所有可能的情况，从而避免了递归或者重复
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] = min(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j]
    return triangle[0][0]
print(minimumTotal(a))
