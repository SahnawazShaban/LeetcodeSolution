class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []  # A list to store the triplets found.
        nums.sort()  # Sort the input array.

        # Iterate over the input array and fix the first element of the triplet.
        for idx, val in enumerate(nums):

            # Skip duplicate elements.
            if idx > 0 and val == nums[idx - 1]:
                continue

            # Initialize the left and right pointers.
            l = idx + 1
            r = len(nums) - 1

            # Keep the sum of the three elements equal to zero.
            while l < r:
                temp = val + nums[l] + nums[r]

                # If the sum is less than zero, increment the left pointer.
                if temp < 0:
                    l += 1

                # If the sum is greater than zero, decrement the right pointer.
                elif temp > 0:
                    r -= 1

                # Otherwise, the sum is equal to zero and we have found a triplet.
                else:
                    # Add the triplet to the result list.
                    result.append([val, nums[l], nums[r]])

                    # Increment the left pointer and skip duplicate elements.
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result
        