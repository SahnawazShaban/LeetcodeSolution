class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        goal = nums[0]

        for i in range(1,len(nums)):
            if goal == 0:
                return False

            goal -= 1

            goal = max(goal,nums[i])

        return True
        