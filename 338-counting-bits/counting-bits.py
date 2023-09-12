class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]  # Initialize the result array.

        for i in range(1, n + 1):  # Iterate over all numbers from 1 to n.
            j = i  # Initialize a copy of i.
            temp = ""  # Initialize a string to store the binary representation of j.

            while j != 0:  # Iterate until j is 0.
                bit = j & 1  # Get the least significant bit of j.
                temp += str(bit)  # Append bit to temp.
                count = temp.count("1")  # Count the number of "1"s in temp.
                j = j >> 1  # Shift j to the right by one bit.
            res.append(count)  # Append count to the result array.

        return res
