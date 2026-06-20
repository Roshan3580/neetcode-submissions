class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            number = nums[:i] + nums[i+1:]
            product = 1
            for j in number:
                product *= j
            res.append(product)
        return res