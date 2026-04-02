class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = 0
        strSet = set()
        L = 0

        for R in range(len(s)):
            
            while s[R] in strSet:
                strSet.remove(s[L])
                L += 1
            
            strSet.add(s[R])
            length = max(length, len(strSet))            

        return length

