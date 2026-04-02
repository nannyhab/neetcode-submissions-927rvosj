class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        maxSum = nums[0]

        for n in range(len(nums)):

            curSum = max(curSum, 0) + nums[n]
            maxSum = max(curSum, maxSum)
        
        return maxSum
