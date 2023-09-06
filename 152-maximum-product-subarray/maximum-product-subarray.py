class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize variables to keep track of the maximum and minimum products.
        max_product = nums[0]  # Initialize max_product to the first element.
        min_product = nums[0]  # Initialize min_product to the first element.

        # Initialize the result to the first element since it's the only element considered.
        result = nums[0]

        # Loop through the elements in the array starting from the second element.
        for i in range(1, len(nums)):
            # If the current number is negative, we swap max_product and min_product.
            # This is because multiplying by a negative number can flip the maximum and minimum products.
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Calculate the new maximum and minimum products ending at the current position.
            max_product = max(nums[i], max_product * nums[i])  # Include the current number in the max product.
            min_product = min(nums[i], min_product * nums[i])  # Include the current number in the min product.

            # Update the overall result by taking the maximum of the current result and max_product.
            result = max(result, max_product)

        return result
            