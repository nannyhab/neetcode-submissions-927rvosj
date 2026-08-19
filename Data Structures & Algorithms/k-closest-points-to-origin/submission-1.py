class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        mapping = [(0,0) for _ in points]
        results = []
        
        indx = 0
        for xi,yi in points:
            euclidian = math.sqrt((xi-0)**2 + (yi-0)**2)
            mapping[indx] = (euclidian, indx)
            indx += 1
        
        heapq.heapify(mapping)

        while len(results) < k:
            euclidian,indx = heapq.heappop(mapping)
            results.append(points[indx])
        
        return results
            
            



        