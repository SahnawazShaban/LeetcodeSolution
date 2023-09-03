class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty (None), and return False if it is.
        if matrix is None:
            return False

        # Get the number of rows (n) and columns (m) in the matrix.
        n = len(matrix)  # Number of rows
        m = len(matrix[0])  # Number of columns

        # Initialize two pointers for binary search.
        low = 0
        high = (n * m) - 1

        while low <= high:
            # Calculate the middle index of the flattened matrix.
            mid = (low + high) // 2

            # Convert the flattened index back to row and column.
            mid_row, mid_col = divmod(mid, m)

            # Check if the element at the middle index is equal to the target.
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                # If the middle element is greater than the target, search in the left half.
                high = mid - 1
            else:
                # If the middle element is less than the target, search in the right half.
                low = mid + 1

        # If the target is not found in the matrix, return False.
        return False

# Example usage:
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# target = 3
# result = searchMatrix(matrix, target)
# print(result)  # Output will be True
