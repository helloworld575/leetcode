import math
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if (len(s) <= numRows or numRows <= 1):
        return s
    t = int(math.ceil(len(s) / (numRows + numRows - 2)))
    a = []
    ta = [0] * (t * (numRows - 1))
    for i in range(numRows):
        a.append(ta.copy())
    state = 0
    row = 0
    column = 0
    for i in s:
        a[row][column] = '' + i
        if state == 0:
            row += 1
            if row >= numRows:
                row -= 2
                column += 1
                state = 1
        elif state == 1:
            row -= 1
            column += 1
            if row == -1:
                state = 0
                column -= 1
                row += 2
    ans = ''
    for i in a:
        for j in i:
            if j != 0:
                ans += j
    return ans

s = "PAYPALISHIRING"
numRows = 3
print(convert(s,numRows))