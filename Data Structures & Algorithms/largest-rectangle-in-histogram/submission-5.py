class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        leftStack = [-1] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftStack[i] = stack[-1]
            stack.append(i)

        stack = []
        rightStack = [len(heights)] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightStack[i] = stack[-1]
            stack.append(i)
        maxArea = 0
        for i in range(len(heights)):
            r = rightStack[i] - 1
            l = leftStack[i] + 1
            maxArea = max((r - l + 1) * heights[i], maxArea)
        return maxArea