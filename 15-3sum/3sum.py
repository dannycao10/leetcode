class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                continue
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
        
        return res