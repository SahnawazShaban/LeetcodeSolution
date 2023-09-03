class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum sum and the current sum.
        max_sum = nums[0]  # Rename 'maxi' to 'max_sum' for clarity
        current_sum = 0  # Rename 'sum1' to 'current_sum' for clarity

        # Loop through the input array 'nums'.
        for i in range(len(nums)):
            # If the current sum becomes negative, reset it to zero.
            if current_sum < 0:
                current_sum = 0

            # Add the current element to the current sum.
            current_sum += nums[i]

            # Update the maximum sum if the current sum is greater.
            max_sum = max(max_sum, current_sum)

        # Return the maximum sum found.
        return max_sum
        
        