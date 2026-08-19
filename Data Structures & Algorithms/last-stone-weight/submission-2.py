class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            newStone = first - second
            if newStone > 0:
                heapq.heappush_max(stones, newStone)
        heapq.heappush_max(stones,0)
        return stones[0]


        