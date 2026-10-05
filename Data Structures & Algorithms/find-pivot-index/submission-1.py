class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSide = 0
        total = sum(nums)

        for index in range(len(nums)):
            if leftSide == total - nums[index] - leftSide:
                return index
            leftSide += nums[index]
        return -1