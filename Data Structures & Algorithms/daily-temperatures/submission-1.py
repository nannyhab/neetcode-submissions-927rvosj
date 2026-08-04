class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = [] #[index,temp]

        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                result[stackIdx] = index - stackIdx

            stack.append([index,temp])

        return result