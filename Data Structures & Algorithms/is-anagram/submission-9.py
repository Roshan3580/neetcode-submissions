class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for char in s:
            hashmap1[char] = hashmap1.get(char, 0) + 1
        for char in t:
            hashmap2[char] = hashmap2.get(char, 0) + 1
        return hashmap1 == hashmap2