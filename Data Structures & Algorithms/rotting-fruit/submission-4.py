class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshFruit = 0
        minutes = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    q.append([row,col])
        print(q)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and freshFruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rowF = r + dr
                    colF = c + dc
                    if 0 <= rowF < rows and 0 <= colF < cols and grid[rowF][colF] == 1:
                        grid[rowF][colF] = 2
                        q.append([rowF,colF])
                        freshFruit -= 1
            minutes += 1
        print(minutes)
        print(freshFruit)
        return minutes if freshFruit == 0 else -1


            


