class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = dict()
        set2 = dict()
        for char1 in s:
            if char1 in set1:
                set1[char1] += 1
            else:
                set1[char1] = 1
        for char2 in t:
            if char2 in set2:
                set2[char2] += 1
            else:
                set2[char2] = 1
        
        return set1 == set2