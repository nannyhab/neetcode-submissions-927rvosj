class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set()
        longest = 0

        for i in range(len(nums)):
            hashSet.add(nums[i])
        
        for j in range(len(nums)):
            val = nums[j]
            if val - 1 not in hashSet:
                counter = 1
                while val + 1 in hashSet:
                    counter += 1
                    val += 1
                longest = max(longest, counter)
        return longest