class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_seq = 0
        seq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                seq += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_seq = max(seq, max_seq)
                seq = 1
        return max(max_seq, seq)
