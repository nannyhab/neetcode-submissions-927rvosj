class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        uniqueChars = set()
        largestNum = 0
        L = 0

        for R in range(len(s)):

            while s[R] in uniqueChars:
                uniqueChars.remove(s[L])
                L += 1

            uniqueChars.add(s[R])
            largestNum = max(R-L+1, largestNum)
        
        return largestNum








