class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"(":")",
                    "{":"}",
                    "[":"]"}
        stack = [] 

        for i in range(len(s)):

            if s[i] in hashMap.values():
                if len(stack) <= 0:
                    return False
                if hashMap[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        if len(stack) != 0: 
            return False

        return True

            
        




        