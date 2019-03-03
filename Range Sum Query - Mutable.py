class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums = self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])



obj = NumArray([-1,1,3,4])
obj.update(1,3)
param_2 = obj.sumRange(1,4)

