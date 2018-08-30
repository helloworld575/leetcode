deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

def openLock(deadends,target):
    nums = "0123456789"
    tmp="0000"
    num = 0
    ends = set(deadends)
    while True:
        if tmp==target:
            return num

    return 0