class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        if len(nums) < 3:
            return []

        for idx, val in enumerate(nums):
            if(idx > 0 and val == nums[idx-1]):
                continue

            l = idx+1
            r = len(nums)-1

            while (l<r):
                temp = val + nums[l] + nums[r]

                if(temp < 0):
                    l += 1
                elif(temp > 0):
                    r -= 1
                else:
                    result.append([val,nums[l],nums[r]])
                    l += 1
                    while(nums[l] == nums[l-1] and l<r):
                        l += 1
                    
        return result
        