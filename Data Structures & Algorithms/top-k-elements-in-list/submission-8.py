class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_list = []
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for key, value in hashmap.items():
            freq_list.append((value, key))
        freq_list.sort()
        freq_list.reverse()
        print(freq_list)
        for i in range(k):
            result.append(freq_list[i][1])
        return result

