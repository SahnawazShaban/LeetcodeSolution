class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, l and r, at the beginning and end of the height list.
        l = 0
        r = len(height) - 1

        # Initialize a variable to store the maximum container volume found.
        result = 0

        # Loop until the left and right pointers meet or cross.
        while l < r:
            # Calculate the volume of the container formed by the lines at positions l and r.
            # The volume is determined by the length (r - l) and the minimum of the two heights.
            rec_formula = (r - l) * min(height[l], height[r])

            # Update the result variable with the maximum volume found so far.
            result = max(result, rec_formula)

            # Move the pointers inward based on the height of the lines:
            # If the left line is shorter, increment l to potentially find a higher line on the left side.
            # Otherwise, decrement r to potentially find a higher line on the right side.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        # Return the maximum container volume found.
        return result