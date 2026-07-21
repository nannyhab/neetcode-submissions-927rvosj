class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       hashMapS = {}
       hashMapT = {}

       if len(s) != len(t): return False

       for i in range(len(s)):
            if s[i] in hashMapS:
                hashMapS[s[i]] += 1
            else:
                hashMapS[s[i]] = 1

       for j in range(len(t)):
        if t[j] in hashMapT:
            hashMapT[t[j]] += 1
        else:
            hashMapT[t[j]] = 1    
        
       for char in s:
        if char not in hashMapT:
            return False 
        if hashMapS[char] != hashMapT[char]:
            return False
        

       return True