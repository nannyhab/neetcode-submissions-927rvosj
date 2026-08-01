class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        maxSubstring = 0
        hashSet = set()

        while R < len(s):
            if s[R] not in hashSet:
                hashSet.add(s[R])
                maxSubstring = max(maxSubstring,len(hashSet))
                R+=1
            else:
                while s[L] != s[R]:
                    hashSet.remove(s[L])
                    L+=1
                L+=1
                hashSet.add(s[R])
                R+=1
        return maxSubstring



