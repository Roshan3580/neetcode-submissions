class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            height = heights[i]
            rightMost = i
            leftMost = i

            while rightMost < len(heights) and height <= heights[rightMost]:
                rightMost += 1
            while leftMost >= 0 and height <= heights[leftMost]:
                leftMost -= 1
            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))

        return maxArea