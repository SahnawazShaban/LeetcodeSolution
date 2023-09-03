class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the values and their corresponding indices.
        temp_dict = {}
        
        # Iterate through the list 'nums' using enumerate to get both the index and value.
        for idx, value in enumerate(nums):
            # Calculate the complement, which is the value needed to reach the target.
            complement = target - value
            
            # Check if the complement is already in the dictionary.
            if complement in temp_dict:
                # If found, return a list containing the indices of the complement and the current value.
                return [temp_dict[complement], idx]
            
            # If the complement is not found, store the current value and its index in the dictionary.
            temp_dict[value] = idx

    # Example usage:
    # Given nums = [2, 7, 11, 15] and target = 9
    # The function should return [0, 1] because nums[0] + nums[1] == 9.

    # The function uses a dictionary to keep track of values and their indices.
    # It iterates through 'nums', calculates the complement for each value, and checks if the complement exists in the dictionary.
    # If found, it returns the indices of the complement and the current value.