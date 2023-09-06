class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize an empty list called 'output' to store the result.
        output = [1]  # Initialize the right product as 1.

        # Calculate the product of all elements to the right of each element.
        for i in range(len(nums)-1, 0, -1):
            # Append the current product to the 'output' list.
            output.append(output[-1] * nums[i])

        # Reverse the 'output' list to get the product of all elements to the right.
        output = output[::-1]

        # Initialize a variable 'left' to store the product of all elements to the left.
        left = 1

        # Calculate the final result, which is the product of elements to the left
        # and right for each element in the 'nums' list.
        for i in range(len(nums)):
            output[i] = output[i] * left  # Multiply the right product by the left product.
            left *= nums[i]  # Update the left product by multiplying it with the current element.

        return output  # Return the final result as a list.