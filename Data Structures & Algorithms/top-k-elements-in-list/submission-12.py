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
            if freq[i]:
                result += (freq[i])
                if len(result) == k:
                    break
            else:
                continue
        return result
            