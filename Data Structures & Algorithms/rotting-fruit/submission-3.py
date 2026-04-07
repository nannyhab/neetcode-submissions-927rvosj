class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        freshFruit = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    freshFruit += 1

        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        while queue and freshFruit > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr,dc in directions:
                    if dr+row in range(rows) and dc+col in range(cols) and grid[dr+row][dc+col] == 1:
                        queue.append((dr+row, dc+col))
                        freshFruit -= 1
                        grid[dr+row][dc+col] = 2

            minutes += 1

        if freshFruit != 0:
            return -1 
        return minutes
        