class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefixSums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        valueLeft = self.prefixSums[left-1] if left > 0 else 0
        valueRight = self.prefixSums[right]
        return (valueRight - valueLeft)


        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)