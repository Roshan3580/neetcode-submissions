class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = []
        for n in nums:
            if n not in hashmap:
                hashmap.append(n)
            else:
                continue
        hashmap.sort()
        print(hashmap)
        result = 0
        if hashmap:
            potential = [hashmap[0]]
        else:
            return 0
        for i in range(1, len(hashmap)):
            if hashmap[i] == hashmap[i-1] + 1:
                potential.append(hashmap[i])
                print(potential)
            else:
                if result < len(potential):
                    result = len(potential)
                    potential = [hashmap[i]]
                else:
                    potential = [hashmap[i]]
        if len(potential) > result:
            result = len(potential)
        return result

            
        