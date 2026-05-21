class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        for i in s1:
            hashmap1[i] = hashmap1.get(i, 0) + 1
        
        need = len(hashmap1)
        for i in range(len(s2)):
            hashmap2, current = {}, 0
            for j in range(i, len(s2)):
                hashmap2[s2[j]] = 1 + hashmap2.get(s2[j], 0)
                if hashmap1.get(s2[j], 0) < hashmap2[s2[j]]:
                    break
                if hashmap1.get(s2[j], 0) == hashmap2[s2[j]]:
                    current += 1
                if current == need:
                    return True
        return False
