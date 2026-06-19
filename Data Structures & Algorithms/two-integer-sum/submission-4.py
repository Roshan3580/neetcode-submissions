class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {nums[0]: 0}
        for i in range(1, len(nums)):
            req = target - nums[i]
            if req in comp:
                return [comp[req], i]
            else:
                comp[nums[i]] = i
