class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        numSum = nums[0] 

        for R in range(len(nums)):
            curSum = max(curSum, 0)
            curSum += nums[R]
            numSum = max(numSum, curSum)

        return numSum


