class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        L = 0
        result = 0 

        for R in range(len(s)):
            hashMap[s[R]] = 1 + hashMap.get(s[R], 0)

            if (R - L + 1) - max(hashMap.values()) > k:
                hashMap[s[L]] -= 1
                L+=1
            result = max(result, R-L+1)
        return result

        
        