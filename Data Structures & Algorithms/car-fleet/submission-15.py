class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[pos,spd] for pos,spd in zip(position, speed)]
        cars.sort(reverse=True)

        for pos, speed in cars:
            rate = (target - pos) / speed
            stack.append(rate)

            if len(stack) > 1 and stack[-2] >= rate:
                stack.pop()

        return len(stack)
            