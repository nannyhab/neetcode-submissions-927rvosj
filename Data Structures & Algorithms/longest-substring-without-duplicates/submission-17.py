class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substringMap = {}
        longest = 0
        L = 0

        for R in range(len(s)):

            while s[R] in substringMap:
                substringMap.pop(s[L])
                L += 1

            substringMap[s[R]] = 1
            longest = max(R - L + 1, longest)
        return longest










