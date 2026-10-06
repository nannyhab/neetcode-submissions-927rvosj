class Solution:
    def rob(self, nums: List[int]) -> int:
        robOption1 = 0
        robOption2 = 0

        for num in nums:
            temp = max(robOption1 + num, robOption2)
            robOption1 = robOption2
            robOption2 = temp
        
        return robOption2