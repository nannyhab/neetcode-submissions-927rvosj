class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        minimum = nums[0]

        while L <= R:
            m = (L + R) // 2
            minimum = min(minimum,nums[m])
            if nums[m] > nums[R]:
                L = m+1
                print(f"m larger than r, nums[m] = {nums[m]}")
            else:
                R = m-1
                print(f"m smaller than r, nums[m] = {nums[m]}")
        return minimum