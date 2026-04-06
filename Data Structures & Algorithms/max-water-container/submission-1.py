class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        largest = 0

        while L < R:
            
            volume = (R-L) * min(heights[L], heights[R])
            print(f"volume is {volume}")
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            largest = max(volume, largest)
        return largest
        