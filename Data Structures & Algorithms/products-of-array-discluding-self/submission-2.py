class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        prefix_product = 1
        suffix_product = 1
        result = []
        for n in nums:
            prefix.append(prefix_product)
            prefix_product *= n
        for i in range(len(nums)-1, -1, -1):
            suffix.append(suffix_product)
            suffix_product *= nums[i]
        suffix = suffix[::-1]
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result