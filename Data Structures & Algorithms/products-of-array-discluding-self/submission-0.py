class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            num = nums[:i] + nums[i+1:]
            product = 1
            for n in num:
                product *= n
            result.append(product)
        return result