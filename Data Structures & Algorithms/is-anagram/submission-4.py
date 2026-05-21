class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for first in s:
            if first in hashmap1:
                hashmap1[first] += 1
            else:
                hashmap1[first] = 1
        for second in t:
            if second in hashmap2:
                hashmap2[second] += 1
            else:
                hashmap2[second] = 1
        print(hashmap1)
        print(hashmap2)
        return hashmap1 == hashmap2