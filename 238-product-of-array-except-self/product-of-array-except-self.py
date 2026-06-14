class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeros = 0

        for n in nums:
            if n == 0:
                numZeros += 1
            else:
                totalProduct *= n
        
        if numZeros > 1:
            return [0] * len(nums)
        
        res = []

        for n in nums:
            if numZeros:
                if n != 0:
                    res.append(0)
                else:
                    res.append(totalProduct)
            else:
                res.append(totalProduct // n)
        
        return res