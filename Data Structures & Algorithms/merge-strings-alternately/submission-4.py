class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = 0
        R = 0

        returnString = ""

        while L < len(word1) and R < len(word2):

            returnString += word1[L] + word2[R]
            L += 1
            R += 1
        
        while L < len(word1):
            returnString += word1[L]
            L += 1
        
        while R < len(word2):
            returnString += word2[R]
            R += 1
        
        return returnString


            
