class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        numOfIslands = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    q.append([row,col])
                    numOfIslands += 1
                    while q:
                        cr, cc = q.popleft()
                        grid[cr][cc] = "0"

                        for dr, dc in directions:
                            tRow = cr+dr
                            tCol = cc + dc
                            if 0 <= tRow < rows and 0 <= tCol < cols and grid[tRow][tCol] == "1":
                                q.append([tRow,tCol])
                                grid[tRow][tCol] = "0"
        
        return numOfIslands