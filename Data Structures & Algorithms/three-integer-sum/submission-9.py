class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = set()
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    hashmap.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        for n in hashmap:
            result.append(list(n))
        return result
