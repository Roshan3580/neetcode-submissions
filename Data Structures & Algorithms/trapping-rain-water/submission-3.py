class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        preMax = [0] * len(height)
        postMax = [0] * len(height)

        preMax[0] = height[0]
        postMax[-1] = height[-1]
        for i in range(1, len(height)):
            preMax[i] = max(preMax[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            postMax[i] = max(postMax[i+1], height[i])
        for i in range(len(height)):
            water += min(postMax[i], preMax[i]) - height[i]
        
        return water

