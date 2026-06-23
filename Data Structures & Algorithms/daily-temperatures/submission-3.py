class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_ind, prev_temp = stack.pop()
                result[prev_ind] = ind - prev_ind
            stack.append([ind, temp])

        return result