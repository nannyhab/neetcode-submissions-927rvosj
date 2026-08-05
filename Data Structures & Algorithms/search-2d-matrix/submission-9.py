class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        topRow = 0
        bottomRow = len(matrix) - 1
        row = 0
        while topRow <= bottomRow:
            row = (topRow + bottomRow) // 2
            if target > matrix[row][-1]:
                topRow = row + 1
            elif target < matrix[row][0]:
                bottomRow = row - 1
            else:
                break

        L = 0
        R = len(matrix[0]) - 1
        while L <= R:
            m = (L+R) // 2
            print(f"m is {m}")
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                R = m - 1
                print(f"R is {R}")
            else:
                L = m + 1
                print(f"L is {L}")
        return False
            
        
