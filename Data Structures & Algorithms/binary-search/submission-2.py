class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            split = (L+R) // 2

            if nums[split] == target:
                return split
            elif nums[split] > target:
                R = split - 1
            else:
                L = split + 1
        return -1