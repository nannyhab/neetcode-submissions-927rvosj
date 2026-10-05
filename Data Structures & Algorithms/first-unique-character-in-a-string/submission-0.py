class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for char in s:
            hashMap[char] = hashMap.get(char,0) + 1
        
        for index in range(len(s)): 
            if hashMap[s[index]] == 1:
                return index
            
        return -1