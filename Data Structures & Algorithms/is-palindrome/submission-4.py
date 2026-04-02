class Solution:
    def isPalindrome(self, s: str) -> bool:

        R = len(s) - 1
        L = 0

        while L < R:
            
            if not s[L].isalnum():
                L  += 1
                continue
            
            if not s[R].isalnum():
                R  -= 1
                continue

            if s[L].lower() != s[R].lower() and s[L].isalnum() and s[R].isalnum():
                print(f"L is {s[L]}")
                print(f"R is {s[R]}")
                return False
            
            R -= 1
            L += 1
        
        return True
        