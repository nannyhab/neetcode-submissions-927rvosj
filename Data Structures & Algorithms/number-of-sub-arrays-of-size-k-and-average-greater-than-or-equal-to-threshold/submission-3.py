class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window = [0]
        L = 0
        counter = 0

        for R in range(len(arr)):

            if R - L + 1 > k:
                window[0] -= arr[L]
                L += 1

            if R + 1 >= k and (window[0] + arr[R]) / k >= threshold:
                counter += 1
            
            aggregate = window[0] + arr[R]
            window[0] = aggregate
        
        return counter