class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        results = []
        minheap = []
        
        for xi,yi in points:
            euclidian = math.sqrt((xi-0)**2 + (yi-0)**2)
            minheap.append((euclidian, xi, yi))
        
        heapq.heapify(minheap)

        while len(results) < k:
            euclidian,x,y = heapq.heappop(minheap)
            results.append([x,y])
        
        return results
            
            



        