class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1 #this is not coinciding with the piles index, it's concerned with the range that k is, can be between 1 and max(piles)
        R = max(piles)
        result = R

        while L <= R:
            k = (L+R) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                result = min(result,k)
                R = k - 1
            else:
                L = k + 1
        return result



