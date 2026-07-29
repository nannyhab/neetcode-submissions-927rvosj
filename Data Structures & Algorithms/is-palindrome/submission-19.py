class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L = 0
        R = len(s) - 1

        while L <= R:
            if s[L].lower() != s[R].lower():
                if not s[L].isalnum():
                    L +=1
                elif not s[R].isalnum():
                    R-=1
                else:
                    print(f"L is {s[L]} and R is {s[R]}")
                    return False
            else:
                L+=1
                R-=1
        return True
    def alphaNumeric(self, char):
        return (ord("A") <= ord(char) <= ord("Z")) or (ord("a") <= ord(char) <= ord("z")) or (ord("0") <= ord(char) <= ord("9"))