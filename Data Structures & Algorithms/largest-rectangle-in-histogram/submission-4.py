class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                temp_index, temp_height = stack.pop()
                maxArea = max(maxArea, temp_height * (index - temp_index))
                start = temp_index
            stack.append((start, height))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea