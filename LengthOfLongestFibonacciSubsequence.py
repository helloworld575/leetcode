def lenLongestFibSubseq(A):
    # Time Limit Exceeded
    # max = 0
    # now = 0
    # for i in range(0, len(A)):
    #     for j in range(i+1,len(A)):
    #         if A[i]+A[j] in A:
    #             now = 3
    #             tmp1 = j
    #             tmp2 = A.index(A[i]+A[j])
    #             print(A[i])
    #             print(A[j])
    #             while A[tmp1]+A[tmp2] in A:
    #                 print(A[tmp2])
    #                 now+=1
    #                 a = tmp2
    #                 tmp2 = A.index(A[tmp1]+A[tmp2])
    #                 tmp1 = a
    #             if max<now:
    #                 max = now
    #             print("=================")
    # return max
    # BF Time Limit Exceeded
    # S = set(A)
    # ans = 0
    # for i in range(len(A)):
    #     for j in range(i+1,len(A)):
    #         x,y = A[i],A[i]+A[j]
    #         length = 2
    #         while y in set(A):
    #             x,y = y,x+y
    #             length+=1
    #         ans = max(ans,length)
    # return ans if ans>=3 else 0
    S = {x:i for i,x in enumerate(A)}





print(lenLongestFibSubseq([1,2,3,4,5,6,7,8]))