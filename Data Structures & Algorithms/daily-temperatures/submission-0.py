class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
           if len(stack) > 0:
                removeElements = []
                for index in range(len(stack) - 1, -1, -1):
                    #stack = [[0,30]] or [index,value]
                    if temperatures[i] > stack[index][1]:
                        print(f"index {index}")
                        prevDayTempIndex = stack[index][0]
                        numDaysAfter = i - prevDayTempIndex
                        result[prevDayTempIndex] = numDaysAfter
                        removeElements.append([stack[index][0],stack[index][1]])
                
                for element in removeElements:
                    print(f"this is stack: {stack}")
                    stack.remove(element)

           stack.append([i,temperatures[i]])

        return result
