class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        max_seq = 0
        for i in range(len(nums)):
            if nums[i]-1 in hashmap:
                continue
            curr, streak = nums[i], 1
            while True:
                if curr + 1 in hashmap:
                    streak += 1
                    curr += 1
                else:
                    max_seq = max(streak, max_seq)
                    break
        return max_seq