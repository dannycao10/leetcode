class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        storage = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in storage:
                return [storage[diff], i]
            storage[n] = i
        
        return []