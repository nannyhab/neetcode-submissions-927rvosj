class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        hashSet = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            hashSet.add((row,col))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    if dr + row in range(rows) and dc + col in range(cols) and (dr+row, dc + col) not in hashSet and grid[dr+row][dc+col] == "1":
                        hashSet.add((dr+row,dc+col))
                        queue.append((dr+row,dc+col))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in hashSet:
                    bfs(row,col)
                    islands+=1
        
        return islands
