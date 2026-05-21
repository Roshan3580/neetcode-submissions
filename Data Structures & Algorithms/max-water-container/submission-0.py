class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = float('-inf')
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j and (min(heights[i],heights[j])* abs(i-j)) > maximum:
                    maximum = (min(heights[i],heights[j])* abs(i-j))
                else:
                    pass
        return maximum