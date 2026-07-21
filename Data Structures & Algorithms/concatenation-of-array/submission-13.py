class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        conc = []
        for num in range(2):
             for i in range(len(nums)):
                conc.append(nums[i])

        return conc