class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
    
        q = deque()
        q.append([sr,sc])

        rows = len(image)
        cols = len(image[0])
        oldPixelColor = image[sr][sc]
        image[sr][sc] = color 

        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == oldPixelColor:
                    image[nr][nc] = color
                    q.append([nr,nc])
        return image



        
