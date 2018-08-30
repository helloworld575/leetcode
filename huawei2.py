import sys
import collections

def judge(a):
    queue = collections.deque()
    for word in a:
        if word=='(':
            queue.append(a[0])
        elif word==')':
            top = queue.pop()
            if top!='(':
                queue.append(top)
                queue.append(word)
        else:
            return False
        print(queue)
    print("================================================")
    if queue:
        return False
    else:
        return True

for line in sys.stdin:
    a = str(line)
    left = 0
    right = len(a)
    length1 = 0
    length2 = 0
    #left
    while left<right:
        print("left")
        while left<right and a[left]!='(':
            left+=1
        if left>=right:
            break
        if judge(a[left:right]):
            length1 = right-left
            break
        left+=1
    left = 0
    while left<right:
        print("right")
        while a[right]!=')':
            right-=1
        if left>=right:
            break
        if judge(a[left:right]):
            length2 = right-left
            break
    print(length1 if length1>length2 else length2)
