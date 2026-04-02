class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = dict()
        string2 = dict()
        for letter in s:
            if letter not in string1:
                string1[letter] = 1
            else:
                string1[letter] = string1[letter] + 1

        for letter in t:
            if letter not in string2:
                string2[letter] = 1
            else:
                string2[letter] = string2[letter] + 1
        
        if string1 == string2:
            return True
        return False