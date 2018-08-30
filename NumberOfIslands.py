a = [['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']]
# 有点意思，通过将矩阵改变，深度优先将同一个岛屿改变为不同的字符
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count =0
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count+=1
                dfs(grid,i,j)
    return count

def dfs(grid,i,j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
        return
    grid[i][j] = '#'
    dfs(grid,i-1,j)
    dfs(grid,i,j-1)
    dfs(grid,i+1,j)
    dfs(grid,i,j+1)
print(numIslands(a))