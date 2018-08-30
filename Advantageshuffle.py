
A = [2,0,4,1,2]
B = [1,3,0,0,2]
#这个题只需要设定A的顺序，使A>B的数量最多就好
def advantageCount(A,B):
    sortedA = sorted(A)
    sortedB = sorted(B)

    assigned = {b:[] for b in B}
    remain = []
    j = 0
    for a in sortedA:
        if a>sortedB[j]:
            assigned[sortedB[j]].append(a)
            j+=1
        else:
            remain.append(a)
    print(sortedA)
    print(sortedB)
    print(assigned)
    print(remain)
    answer = []
    for b in B:
        if assigned[b]:
            answer.append(assigned[b].pop())
        else:
            answer.append(remain.pop())
    return answer
print(advantageCount(A,B))

