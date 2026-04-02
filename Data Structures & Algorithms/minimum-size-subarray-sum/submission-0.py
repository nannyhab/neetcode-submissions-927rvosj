class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        total = 0
        minNum = float("inf")
        
        for R in range(len(nums)):

            total += nums[R]

            while total >= target:
                minNum = min(R - L + 1, minNum)
                total -= nums[L]
                L += 1
        
        if minNum == float("inf"):
            return 0
        return minNum
                