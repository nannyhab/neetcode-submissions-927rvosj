class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)
        counter = 0
        res = 0
        while counter != k:
            res = heapq.heappop_max(nums)
            counter += 1

        return res
            