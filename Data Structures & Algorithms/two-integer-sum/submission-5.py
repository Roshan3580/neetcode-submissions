class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in comp:
                return [comp[req], i]
            comp[num] = i