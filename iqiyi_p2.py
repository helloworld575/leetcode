# 局长有N种食物，每种食物有Ai份。
#
# 每天局长会吃一份食物，或者买一份食物（即每天只能进行吃或买其中的一种动作），这样过了M天
#
# 现在局长想知道M天后第p种食物的份数排名（从大到小，相同算并列，例如3 3 2，则排名为1 1 3）
#
# N,M,P<=100,Ai<=1000
N,M,P = [int(x) for x in input().split(" ")]
T = []
A = [int(x) for x in input().split(" ")]
for i in range(M):
    oneDay = input().split(" ")
    if oneDay[0]=='A':
        A[int(oneDay[1])-1] += 1
    else:
        A[int(oneDay[1])-1] -= 1
for i in range(len(A)):
    T.append([A[i],i])
ans = -1
TT = sorted(T,key = lambda s:s[0],reverse=True)
i = 0
tmp = 0
print(T)
print(TT)
#########################################################
for i in range(len(TT)):
    if TT[i][1]==P-1:
        ans = i
        tmp = TT[i][0]
        break
while ans>=-1 and TT[ans][0]==tmp:
    ans-=1
print(ans+2)
a='''
3 4 3
5 3 1
B 1
A 2
A 2
A 3
'''