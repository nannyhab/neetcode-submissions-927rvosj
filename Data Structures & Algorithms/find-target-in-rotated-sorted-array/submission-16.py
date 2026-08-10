class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)- 1

        while L <= R:
            m = (L+R) // 2

            if nums[m] == target:
                return m
            
            if nums[L] <= nums[m]:
                if target < nums[L] or target > nums[m]:
                    L = m + 1
                elif target >= nums[L] and target <= nums[m]:
                    R = m - 1
            elif nums[m] <= nums[R]:
                if target < nums[m] or target > nums[R]:
                    R = m - 1
                elif target >= nums[m] and target <= nums[R]:
                    L = m + 1
        return -1
