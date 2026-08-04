class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [[a,b] for a,b in zip(position,speed)]
        cars.sort(reverse = True)

        stack = []
        firstCarPos, firstCarSpd = cars[0]
        if (firstCarPos and firstCarSpd):
            rate = (target - firstCarPos) / firstCarSpd
            stack.append(rate)

        for pos, spd in cars:
            rate = (target - pos) / spd
            
            if stack and stack[-1] < rate:
                stack.append(rate)            

        return len(stack)