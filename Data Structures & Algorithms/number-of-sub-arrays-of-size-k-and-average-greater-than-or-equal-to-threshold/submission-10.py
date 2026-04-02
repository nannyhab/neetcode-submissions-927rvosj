class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        total = 0
        counter = 0
        windowLen = 0
        
        for R in range(len(arr)):
            windowLen = R - L + 1

            if windowLen > k:
                total -= arr[L]
                L += 1
            
            if windowLen >= k and (total + arr[R]) / k >= threshold:
                counter += 1

            total += arr[R]

        return counter
            
       