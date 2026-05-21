class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for i in s:
            if i in hashmap1:
                hashmap1[i] += 1
            else:
                hashmap1[i] = 1
        for i in t:
            if i in hashmap2:
                hashmap2[i] += 1
            else:
                hashmap2[i] = 1
        if hashmap1 == hashmap2:
            return True
        else:
            return False
