class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        row = 0
        matrixM = False

        while top <= bottom:
            row = (top+bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                matrixM = True
                break
        
        if not matrixM:
            return False
        
        L = 0
        R = COLS - 1

        while L <= R:
            m = (L+R) // 2

            if matrix[row][m] > target:
                R = m - 1
            elif matrix[row][m] < target: 
                L = m + 1
            else:
                return True
                
        return False
        
