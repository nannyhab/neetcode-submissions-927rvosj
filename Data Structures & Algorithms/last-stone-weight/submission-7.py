class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)


        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            smash = abs(x-y)
            if smash != 0:
                heapq.heappush_max(stones, smash)
        
        if len(stones) == 1:
            return heapq.heappop_max(stones)
        return 0
        