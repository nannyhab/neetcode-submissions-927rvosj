class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens: 
            
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            elif element == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first/second))
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(element))
        return stack[0]


