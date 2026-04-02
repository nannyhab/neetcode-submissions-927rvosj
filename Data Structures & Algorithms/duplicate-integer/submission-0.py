class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for item in nums:
            if item in dupes:
                return True
            else:
                dupes.add(item)
        return False