class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_index = len(nums)*[0]
        for n in nums:
            if seen_index[n] == -1:
                return n
            seen_index[n] = -1