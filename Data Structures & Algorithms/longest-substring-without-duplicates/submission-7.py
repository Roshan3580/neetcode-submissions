class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, count, l = 0, 0, 0
        hashmap = set()

        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap.add(s[r])
                count += 1
                res = max(res, count)
            else:
                while s[r] in hashmap:
                    hashmap.remove(s[l])
                    count -= 1
                    l += 1
                hashmap.add(s[r])
                count += 1
                res = max(res, count)
        return res