class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        curSum = 0
        for n in range(len(nums)):

            curSum = max(curSum, 0) + nums[n]
            print(f"{curSum}")
            if curSum > maxSum:
                maxSum = curSum
        
        return maxSum
