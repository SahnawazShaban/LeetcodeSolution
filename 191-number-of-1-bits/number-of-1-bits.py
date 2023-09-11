class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            bit = n&1
            count += bit
            n = n >> 1

        return count
        