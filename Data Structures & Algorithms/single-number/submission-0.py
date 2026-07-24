class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if num in stack:
                stack.remove(num)
            else:
                stack.append(num)
        return stack[0]