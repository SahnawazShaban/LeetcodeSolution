class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False  # Handle the case of an empty matrix

        n = len(matrix) - 1
        m = len(matrix[0])

        rows = 0
        cols = m - 1

        while cols >= 0 and rows <= n:
            if target == matrix[rows][cols]:
                return True
            elif target > matrix[rows][cols]:
                rows += 1  # Move down in the matrix
            else:
                cols -= 1  # Move left in the matrix

        return False  # If the target is not found in the matrix

        