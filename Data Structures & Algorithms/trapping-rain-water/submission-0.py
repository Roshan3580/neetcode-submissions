class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        
        maxPrefix = [0] * length
        maxSuffix = [0] * length

        maxPrefix[0] = height[0]
        for i in range(1, length):
            maxPrefix[i] = max(maxPrefix[i-1], height[i])

        maxSuffix[length-1] = height[length-1]
        for i in range(length - 2, -1, -1):
            maxSuffix[i] = max(maxSuffix[i+1], height[i])
        result = 0
        for n in range(length):
            result += min(maxPrefix[n], maxSuffix[n]) - height[n]

        return result