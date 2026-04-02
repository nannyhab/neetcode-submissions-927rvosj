class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sumVal = nums[i] + nums[j] 
                if sumVal == target:
                    return [i,j]
                
        