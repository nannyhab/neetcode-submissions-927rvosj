class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closethenopen = {"}":"{", ")":"(", "]":"["
        }

        for char in s:

            if char in closethenopen:
                if stack and  closethenopen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0        