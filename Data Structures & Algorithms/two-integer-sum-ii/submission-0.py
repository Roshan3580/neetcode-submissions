class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            difference = target - numbers[n]
            for j in range(len(numbers)):
                if n != j and numbers[j] == difference:
                    return [n+1, j+1]
                else:
                    continue
 