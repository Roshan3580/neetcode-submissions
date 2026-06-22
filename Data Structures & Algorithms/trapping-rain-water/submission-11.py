class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        w = 0

        l, r = 0, len(height)-1
        mL, mR = height[l], height[r]

        while l < r:
            if mL <= mR:
                l += 1
                mL = max(mL, height[l])
                w += mL - height[l]
            else:
                r -= 1
                mR = max(mR, height[r])
                w += mR - height[r]
        return w