class Solution:
    def countBits(self, n: int) -> List[int]:
        # # APPROACH - 1
        # # TIME COMPLEXITY : O(nlog(n))
        # # SPACE COMPLEXITY : O(n) : The space complexity of the code is O(n), where n is the number of bits in the binary representation of n. The result array stores n elements.

        # res = [0]  # This line allocates an array of size n.

        # for i in range(1, n + 1):  # Iterate over all numbers from 1 to n.
        #     j = i  # Initialize a copy of i.
        #     temp = ""  # Initialize a string to store the binary representation of j.

        #     while j != 0:  # Iterate until j is 0.
        #         bit = j & 1  # Get the least significant bit of j.
        #         temp += str(bit)  # Append bit to temp.
        #         count = temp.count("1")  # Count the number of "1"s in temp.
        #         j = j >> 1  # Shift j to the right by one bit.
        #     res.append(count)  # Append count to the result array.

        # APPROACH - 2
        # TIME COMPLEXITY : O(n)
        # SPACE COMPLEXITY : O(n) 
        res = [] # This line allocates an array of size n.

        for i in range(n + 1):
            temp = bin(i).count("1") #This line takes O(1) time to convert i to its binary representation and count the number of "1"s in the representation.
            res.append(temp)
        
        return res
