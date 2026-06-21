class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        
        for i in range(len(height)):
            maxLeft = maxRight = height[i]
            for j in range(0, i):
                maxLeft = max(height[j], maxLeft)
                for k in range(i, len(height)):
                    maxRight = max(height[k], maxRight)
            water += min(maxLeft, maxRight) - height[i]

        return water