class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0

        while(l<r):
            recFormula = (r-l) * min(height[l],height[r])
            result = max(result,recFormula)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return result