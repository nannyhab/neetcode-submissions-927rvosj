class Solution:
    def validPalindrome(self, s: str) -> bool:

        deletedCharBool = False
        L = 0
        R = len(s) -1

        while L < R:

            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                skipL = s[L+1:R+1]
                skipR = s[L:R]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            L+=1
            R-=1     
        return True   
    
    def reverseString(self, string):
        L = 0
        R = len(string)-1

        while L < R:
            tmp = string[L]
            string[L] = string[R]
            string[R] = tmp
            L += 1
            R -= 1
        return string