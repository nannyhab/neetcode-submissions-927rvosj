class Solution:       

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        hashSet = set()

        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    if dr + row in range(rows) and (dr+row, col) not in hashSet and grid[dr+row][col] == "1":
                        hashSet.add((dr+row,col))
                        queue.append((dr+row,col))
                        print(f"row direction is 1{(dr+row,col)}")
                    elif dc + col in range(cols) and (row, dc + col) not in hashSet and grid[row][dc+col] == "1":
                        hashSet.add((row, dc+col))
                        queue.append((row, dc+col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in hashSet:
                    bfs(row,col)
                    islands += 1
                    
        return islands
        
        

        