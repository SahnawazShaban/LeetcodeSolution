class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(matrix[r][c])

            result.append(temp)

        return result
        

        