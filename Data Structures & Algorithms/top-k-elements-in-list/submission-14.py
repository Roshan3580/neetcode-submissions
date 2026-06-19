class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq=[[] for i in range(len(nums)+1)]
        result = []
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, value in count.items():
            freq[value].append(key)
        print(freq)
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            