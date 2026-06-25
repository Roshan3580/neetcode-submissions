class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        l, r = 0, len(s1) - 1

        for i in range(r + 1):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        while r < len(s2):
            if count1 == count2:
                return True

            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]

            l += 1

            if r + 1 < len(s2):
                r += 1
                count2[s2[r]] = count2.get(s2[r], 0) + 1
            else:
                break
        return False
                        