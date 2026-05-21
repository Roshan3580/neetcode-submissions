class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            print(nums)
            number = abs(nums[i]) - 1
            if nums[number] < 0:
                return abs(nums[i])
            else:
                nums[number] *= -1
        