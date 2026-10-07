class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        newArr = []
        
        i=0
        for x,y in points:
            euclid = math.sqrt((x-0)**2 + (y-0)**2)
            newArr.append((euclid,i))
            i+=1
        
        heapq.heapify(newArr)
        print(newArr)
        counter = 0
        while counter != k:
            euclid, i = heapq.heappop(newArr)
            res.append(points[i])
            counter += 1
        
        return res
