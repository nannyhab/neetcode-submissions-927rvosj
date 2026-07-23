class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for indx,val in enumerate(nums):
            complement = target-val
            if complement in hashMap:
                return [hashMap[complement],indx] 
            hashMap[val] = indx
