class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxSum = 0
        L = 0
        buffer = 0

        for R in range(len(nums)):
            
            if nums[R] == 0:
                buffer += 1
                while buffer > k:
                    if nums[L] == 0:
                        buffer -= 1
                    L += 1
            
            maxSum = max(maxSum, R - L + 1)
        return maxSum
