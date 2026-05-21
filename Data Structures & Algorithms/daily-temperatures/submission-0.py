class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if i != j and temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result
                