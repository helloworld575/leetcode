
s = 3
nums = [1,1]
# s = 80
# nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
# s = 11
# nums = [1,2,3,4,5]
def miniSubSum(s,nums):
    Min = 0
    Max = 0
    Length = 0
    Sum = 0
    L_Array = []
    if nums ==[]:
        return 0
    # 此处逻辑搞了我好久，fuckyou
    while Sum<s:
        Max+=1
        if Max>len(nums):
            return 0
        Sum+=nums[Max-1]
        Length+=1
        print(Sum,Max)
    L_Array.append(Length)
    print(Min,Max,Length,Sum,L_Array)
    flag = 0
    while Max<=len(nums):
        Sum-=nums[Min]
        Length-=1
        Min+=1
        print(Min, Max, Length, Sum, L_Array, flag)
        while Sum<s:
            if Max>=len(nums):
                flag = 1
                break
            Sum+=nums[Max]
            Max+=1
            Length+=1
        print(Min, Max, Length, Sum, L_Array,flag)
        if flag==1:
            break
        L_Array.append(Length)
    print(L_Array)
    return min(L_Array)

print(miniSubSum(s,nums))