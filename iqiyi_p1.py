# 小C有一张票，这张票的ID是长度为6的字符串，每个字符都是数字，他想让这个ID变成他的辛运ID，所以他就开始更改ID，
# 每一次操作，他可以选择任意一个数字并且替换它。
#
# 如果这个ID的前三位数字之和等于后三位数字之和，那么这个ID就是辛运的。你帮小C求一下，最少需要操作几次，能使ID变成辛运ID


a = input()
l1 = []
l2 = []
num1 = 0
num2 = 0
for i in range(6):
    if i<3:
        num1=num1+int(a[i])
        l1.append(int(a[i]))
    else:
        num2 = num2+int(a[i])
        l2.append(int(a[i]))
l1 = sorted(l1)
l2 = sorted(l2)
if num1<num2:
    nums = l1+l2
    snum = num2-num1
else:
    nums = l2+l1
    snum = num1-num2
if snum==0:
    print(0)
elif snum<=nums[5] or snum<=(9-nums[0]):
    print(1)
elif snum<=(nums[5]+nums[4]) or snum<=(18-nums[0]-nums[1]) or snum<=(9-nums[0]+nums[5]):
    print(2)
else:
    print(3)
# 通过率83%

