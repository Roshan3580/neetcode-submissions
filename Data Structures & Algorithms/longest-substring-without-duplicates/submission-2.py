class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l+= 1
            hashmap.add(s[r])
            count = max(count, r- l + 1)
        return count