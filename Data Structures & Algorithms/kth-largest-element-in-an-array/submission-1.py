class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        popped = 0
        result = 0
        while popped != k:
            result = heapq.heappop_max(nums)
            popped += 1
        
        return result

