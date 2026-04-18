class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
    
        for num in nums:
            new_subsets = []
            for curr in res:
                new_subsets.append(curr + [num])
            res += new_subsets

        return res
        