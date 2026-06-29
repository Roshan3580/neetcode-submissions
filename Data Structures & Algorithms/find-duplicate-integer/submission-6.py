class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = abs(nums[i])
            index = num - 1
            if nums[index] < 0:
                return num
            nums[index] *= -1
